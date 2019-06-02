from itertools import combinations
from functools import lru_cache
from pprint import pprint


def greedy(usb_size, memes):
    """
    Calculate maximal price for USB stick using greedy solution
    :param usb_size: capacity of USB stick in GiB
    :param memes: list of memes data in form (name, size, price), size in MiB, price in caps
    :return: maximal price for USB stick and set of memes names
    """
    usb_size_Mib = 1024*usb_size
    usb_stick_memory_used = 0
    usb_price = 0
    usb_meme_names = set()
    for name, size, price in sorted(memes, key=lambda x: (x[2]/x[1])):
        if usb_stick_memory_used < usb_size_Mib - size:
            usb_stick_memory_used += size
            usb_price += price
            usb_meme_names.update([name])
    return usb_price, usb_meme_names


def brute(usb_size, memes):
    """
    Calculate maximal price for USB stick using brute force solution
    :param usb_size: capacity of USB stick in GiB
    :param memes: list of memes data in form (name, size, price), size in MiB, price in caps
    :return: maximal price for USB stick and set of memes names
    """
    usb_size_Mib = 1024*usb_size
    max_price = 0
    memes_set = set()
    for i in range(len(memes)):
        for comb in combinations(memes, i+1):
            usb_stick_memory_used = sum(meme[1] for meme in comb)
            usb_price = sum(meme[2] for meme in comb)
            if max_price < usb_price and usb_stick_memory_used<usb_size_Mib:
                max_price = usb_price
                memes_set = {meme[0] for meme in comb}
    return max_price, memes_set


def calculate(usb_size, memes):
    """
    Calculate maximal price for USB stick using dynamic solution
    :param usb_size: capacity of USB stick in GiB
    :param memes: list of memes data in form (name, size, price), size in MiB, price in caps
    :return: maximal price for USB stick and set of memes names
    """
    usb_size_Mib = 1024 * usb_size
    memes_size = len(memes)
    previous_values = [[0 for _ in range(usb_size_Mib + 1)] for _ in range(memes_size + 1)]
    previous_names = [[frozenset() for _ in range(usb_size_Mib + 1)] for _ in range(memes_size + 1)]
    for meme_index in range(memes_size + 1):
        for size in range(usb_size_Mib + 1):
            if size == 0 or meme_index == 0:
                previous_values[meme_index][size] = 0
            elif memes[meme_index-1][1] <= size:
                without_item = previous_values[meme_index - 1][size]
                with_item = memes[meme_index-1][2] + previous_values[meme_index - 1][size - memes[meme_index-1][1]]
                if with_item > without_item:
                    previous_values[meme_index][size] = with_item
                    names_set = previous_names[meme_index - 1][size - memes[meme_index-1][1]].copy()
                    previous_names[meme_index][size] = names_set.union([meme_index])
                else:
                    previous_values[meme_index][size] = without_item
                    previous_names[meme_index][size] = previous_names[meme_index - 1][size]
            else:
                previous_values[meme_index][size] = previous_values[meme_index - 1][size]
                previous_names[meme_index][size] = previous_names[meme_index - 1][size]
    best_price = previous_values[memes_size][usb_size_Mib]
    memes_names_set = {memes[index-1][0] for index in previous_names[memes_size][usb_size_Mib]}
    return best_price, memes_names_set


def calculate_recursion(usb_size, memes):
    """
    Calculate maximal price for USB stick using recursion
    :param usb_size: capacity of USB stick in GiB
    :param memes: list of memes data in form (name, size, price), size in MiB, price in caps
    :return: maximal price for USB stick and set of memes names
    """
    usb_size_Mib = 1024 * usb_size
    _, size, prices = zip(*memes)

    @lru_cache()
    def solve(capacity, i=0):
        if capacity < 0:
            return -sum(prices), [] #change that for 0
        if i == len(size):
            return 0, []
        without_item = solve(capacity, i+1)
        if_add_item = solve(capacity - size[i], i+1)
        with_item = if_add_item[0] + prices[i], if_add_item[1]+[i]
        return without_item if without_item[0] > with_item[0] else with_item

    results = solve(usb_size_Mib)
    return results[0], {memes[i][0] for i in results[1]}


if __name__ == '__main__':
    usb_size = 2
    memes = [
        ('rollsafe.jpg', 205, 6),
        ('sad_pepe_compilation.gif', 410, 10),
        ('yodeling.avi', 605, 12),
        ('pepe.jpg', 105, 3),
        ('grumpy_cat.gif', 302, 20),
        ('be_like_bil.avi', 800, 11),
        ('guitar.jpg', 90, 2),
        ('happy_pepe_compilation.gif', 12, 10),
        ('old_spice_guy.avi', 890, 13)
    ]
    pprint(calculate(usb_size, memes))
