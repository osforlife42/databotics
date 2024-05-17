import numpy as np
import time
from multiprocessing import Pool

# time.sleep(1)
def compute_mean(arr):
    return np.mean(arr)

def normal_computation(arr, num_chunks):
    chunks = np.array_split(arr, num_chunks)
    results = [compute_mean(chunk) for chunk in chunks]
    return np.array(results)

def multiprocessing_computation(arr, num_chunks, num_processes):
    chunks = np.array_split(arr, num_chunks)
    with Pool(processes=num_processes) as pool:
        results = pool.map(compute_mean, chunks)
    return np.array(results)

# Create a large sample array
arr = np.random.rand(100000000)

# Set the number of chunks and processes
num_chunks = 4
num_processes = 5

# Normal computation
start_time = time.time()
result_normal = normal_computation(arr, num_chunks)
end_time = time.time()
print(f"Normal computation time: {end_time - start_time:.2f} seconds")

# Multiprocessing computation
start_time = time.time()
result_multiprocessing = multiprocessing_computation(arr, num_chunks, num_processes)
end_time = time.time()
print(f"Multiprocessing computation time: {end_time - start_time:.2f} seconds")


# In my computer - multiprocess worked worse than normal calculation 