import numpy as np

import time

class CircularBuffer:
    def __init__(self, max_size=300, max_seconds=2):
        self.buffer = np.zeros(max_size, dtype=float)
        self.timestamps = np.zeros(max_size, dtype=float)
        self.max_size = max_size
        self.max_seconds = max_seconds
        self.index = 0
        self.size = 0
        
    def add(self, value):
        current_time = time.time()
        self.buffer[self.index] = value
        self.timestamps[self.index] = current_time
        self.index = (self.index + 1) % self.max_size
        if self.size < self.max_size:
            self.size += 1

    def get_data(self):
        current_time = time.time()
        valid_time = current_time - self.max_seconds
        
        if self.size == self.max_size:
            indices = (self.timestamps >= valid_time)
            valid_indices = np.arange(self.max_size)[indices]
            valid_indices_shifted = np.concatenate((valid_indices[self.index:], valid_indices[:self.index])) 
            data = self.buffer[valid_indices_shifted]
            return data
        else:
            print(self.timestamps[:self.size] >= valid_time)
            valid_indices = np.arange(self.size)[self.timestamps[:self.size] >= valid_time]
            return self.buffer[valid_indices]


class MinCircularBuffer(CircularBuffer):
    def __init__(self, max_size=300, max_seconds=2):
        super().__init__(max_size, max_seconds)
        self.min_indices = []  # Store indices of minimum values
        self.min_value = float('inf')

    def add(self, value):
        super().add(value)
        current_index = (self.index - 1) % self.max_size

        # Update min indices
        if not self.min_indices or value < self.buffer[self.min_indices[0]]:
            self.min_indices = [current_index]
        elif value == self.buffer[self.min_indices[0]]:
            self.min_indices.append(current_index)
        
        # Remove outdated min indices
        valid_time = time.time() - self.max_seconds
        while self.min_indices and self.timestamps[self.min_indices[0]] < valid_time:
            self.min_indices.pop(0)

        # Update min value
        if value < self.min_value:
            self.min_value = value

    def get_min_value(self):
        return self.min_value
    

if __name__ == "__main__": 
    # Usage example
    buffer = CircularBuffer(max_size=300, max_seconds=1)
    
    # Simulate adding data at 20 Hz for 10 seconds (200 samples)
    for i in range(200):
        buffer.add(float(i))
        time.sleep(0.01)  # Simulate 20 Hz
    
    # Retrieve the current buffer content
    current_data = buffer.get_data()
    print(current_data)

