import random
import time
from statistics import mean
from main import calculate, calculate_recursion

for size_of_data in [10, 20, 25]:
    print("data size:", size_of_data)
    usb_size = random.randint(1, 4)
    memes = [(str(i), random.randint(100, 800), random.randint(1, 30)) for i in range(size_of_data)]
    for func in [calculate, calculate_recursion]:
        times = []
        results = []
        for iteration in range(15):
            start = time.time()
            result, *_ = func(usb_size, memes)
            delta = time.time() - start
            times.append(delta)
            results.append(result)
        print(f"{func.__name__}", mean(times), mean(results))



