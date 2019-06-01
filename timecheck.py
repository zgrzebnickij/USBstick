from main import calculate, calculate_recursion
import random
import time
from statistics import mean

for size_of_data in [50]:
    print("data size:", size_of_data)
    usb_size = random.randint(1, 4)
    time_calc = []
    result_calc = []
    time_brut = []
    result_brut = []
    time_knapsack = []
    result_knapsack = []
    for iteration in range(10):
        memes = [(str(i), random.randint(100, 800), random.randint(1, 30)) for i in range(size_of_data)]
        for func in [calculate_recursion, calculate, ]:
            start = time.time()
            result, *_ = func(usb_size, memes)
            delta = time.time() - start
            if func == calculate:
                time_calc.append(delta)
                result_calc.append(result)
            else:
                time_brut.append(delta)
                result_brut.append(result)

    print("calculate_recursion:", mean(time_brut), result_brut)
    print("calculate:", mean(time_calc), result_calc)


