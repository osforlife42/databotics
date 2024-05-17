import pytest
import numpy as np
import time
from freezegun import freeze_time
from databotics.circular_buffer import CircularBuffer  # Assuming the class is in a file named circular_buffer.py

@freeze_time("2024-05-24 12:00:00")
def test_add_and_retrieve():
    buffer = CircularBuffer(max_size=10, max_seconds=10)
    
    buffer.add(1.0)
    buffer.add(2.0)
    buffer.add(3.0)
    
    data = buffer.get_data()
    assert np.array_equal(data, np.array([1.0, 2.0, 3.0]))

@freeze_time("2024-05-24 12:00:00")
def test_buffer_overflow():
    buffer = CircularBuffer(max_size=3, max_seconds=10)
    
    buffer.add(1.0)
    buffer.add(2.0)
    buffer.add(3.0)
    buffer.add(4.0)
    
    data = buffer.get_data()
    assert np.array_equal(data, np.array([2.0, 3.0, 4.0]))

@freeze_time("2024-05-24 12:00:00")
def test_time_relevance():
    buffer = CircularBuffer(max_size=10, max_seconds=2)
    
    buffer.add(1.0)
    buffer.add(2.0)
    buffer.add(3.0)
    
    with freeze_time("2024-05-24 12:00:01"):
        buffer.add(4.0)
    
    with freeze_time("2024-05-24 12:00:02.1"):
        buffer.add(5.0)

        data = buffer.get_data()

    assert np.array_equal(data, np.array([4.0, 5.0]))

@freeze_time("2024-05-24 12:00:00")
def test_no_new_data():
    buffer = CircularBuffer(max_size=10, max_seconds=2)
    
    buffer.add(1.0)
    buffer.add(2.0)
    buffer.add(3.0)
    
    with freeze_time("2024-05-24 12:00:04"):
        data = buffer.get_data()
    
    assert len(data) == 0

@freeze_time("2024-05-24 12:00:00")
def test_partial_relevance():
    buffer = CircularBuffer(max_size=10, max_seconds=3)
    
    buffer.add(1.0)
    buffer.add(2.0)
    
    with freeze_time("2024-05-24 12:00:01"):
        buffer.add(3.0)
    
    with freeze_time("2024-05-24 12:00:03"):
        buffer.add(4.0)
    
    with freeze_time("2024-05-24 12:00:03.8"):
        buffer.add(5.0)
    
        data = buffer.get_data()
    assert np.array_equal(data, np.array([3.0, 4.0, 5.0]))

@freeze_time("2024-05-24 12:00:00")
def test_full_buffer_with_relevance():
    max_size = 5
    time_inc = 1.1
    buffer = CircularBuffer(max_size=max_size, max_seconds=3)
    
    for i in range(5):
        with freeze_time(f"2024-05-24 12:00:0{i * time_inc}"):
            buffer.add(float(i+1))
    
    with freeze_time(f"2024-05-24 12:00:0{max_size * time_inc}"):
        buffer.add(6.0)
        data = buffer.get_data()

    assert np.array_equal(data, np.array([4.0, 5.0, 6.0]))

if __name__ == '__main__':
    pytest.main()
