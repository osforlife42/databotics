import time
import numpy as np
import pytest
from databotics.circular_buffer import MinCircularBuffer

@pytest.fixture
def buffer():
    return MinCircularBuffer(max_size=5, max_seconds=2)

def test_add_and_get_min_value(buffer):
    buffer.add(10)
    buffer.add(5)
    buffer.add(8)
    buffer.add(3)
    buffer.add(12)
    assert buffer.get_min_value() == 3

def test_update_min_value(buffer):
    buffer.add(10)
    buffer.add(5)
    buffer.add(8)
    buffer.add(3)
    buffer.add(12)
    time.sleep(1)
    buffer.add(2)
    assert buffer.get_min_value() == 2

def test_outdated_data(buffer):
    buffer.add(10)
    buffer.add(5)
    buffer.add(8)
    buffer.add(3)
    buffer.add(12)
    time.sleep(3)
    buffer.add(2)
    assert buffer.get_min_value() == 2

def test_empty_buffer(buffer):
    assert buffer.get_min_value() is None

if __name__ == "__main__":
    pytest.main()
