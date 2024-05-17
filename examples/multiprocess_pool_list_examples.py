import time
from multiprocessing import Pool


def square_numbers(numbers_list):
    res = []
    for numbers in numbers_list: 
        res.append([x ** 2 for x in numbers])
    return res

# Create a large list of numbers
numbers_lists = [list(range(10**7)) for _ in range(3)]

# Measure time without multiprocessing
start_time = time.time()
result = square_numbers(numbers_lists)
end_time = time.time()

print("Time without multiprocessing:", end_time - start_time)


def square_number(x):
    return x ** 2


# Measure time with multiprocessing
start_time = time.time()

# Use multiprocessing Pool
with Pool() as pool:
    for numbers in numbers_lists: 
        result = pool.map(square_number, numbers)

end_time = time.time()

print("Time with multiprocessing:", end_time - start_time)