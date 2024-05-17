import numpy as np
import time
from concurrent.futures import ThreadPoolExecutor


def square_and_sum_arrays(arrays):
    result = np.zeros_like(arrays[0])
    for array in arrays:
        result += np.square(array)
    return result

def get_mins(arrays):
    return [np.min(array) for array in arrays]
# Create large arrays
arrays = [np.random.rand(3000, 3000) for _ in range(100)]

# Measure time without ThreadPoolExecutor
start_time = time.time()
result = get_mins(arrays)
end_time = time.time()

print("Time without ThreadPoolExecutor:", end_time - start_time)


def square_and_sum_partial_arrays(partial_arrays):
    result = np.zeros_like(partial_arrays[0])
    for array in partial_arrays:
        result += np.square(array)
    return result


# Create medium-sized arrays
arrays = [np.random.rand(3000, 3000) for _ in range(100)]

# Measure time with ThreadPoolExecutor
start_time = time.time()

# Split arrays into chunks for parallel processing
chunks = [arrays[i::5] for i in range(5)]

with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(get_mins, chunk) for chunk in chunks]
    partial_results = [future.result() for future in futures]

# Combine the partial results
result = np.zeros_like(arrays[0])
for partial_result in partial_results:
    result += partial_result

end_time = time.time()

print("Time with ThreadPoolExecutor:", end_time - start_time)