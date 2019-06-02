# USBstick

Python3.7

In _main.py_ there are few functions that calculates the best set of memes, such that the UBS stick can be sold for the highest price.
As arguments function takes USB stick capacity and list of memes in form (str(name), int(size), int(price))
The function return a tuple with total price of memes on USB stick and set of their names

## Description
Functions:

* _brute_force_ - This was the first idea to check all solutions and get exact answer.
It was used to check other algorithms and only for that because it complexity is 2^n where n is number of items
* _greedy_ - Making this solution i tried to find one parameter which can describe all memes.
This solution is quick but inaccurate 
* _calculate_ - In this solution each meme is checked starting from capacity equals 1 MiB.
Two possibilities are checked and better id chosen. Firs one include item in USB stick and add its value to the value from previous meme where capacity was smaller by current meme value.
Second one take its value from the same capacity of previous meme. This solution is efficient because it stores prices of all capacities 
* _calculate_recursion_ - it's similar to calculate function but use recursion and program remembers function calls with the same arguments.

Conclusion:

The best function is _calculate_ because it's more efficient for larger data sets.
Recurrent solution works better but only to some point.


## Examples

Example 1:
```
usb_size = 1
memes = [
    ('rollsafe.jpg', 205, 6),
    ('sad_pepe_compilation.gif', 410, 10),
    ('yodeling.avi', 605, 12)
]

calculate(usb_size, memes)
```
output:
```
(22, {'sad_pepe_compilation.gif', 'yodeling.avi'})
```

Example 2:
```
usb_size = 1
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

calculate(usb_size, memes)
```
output:
```
(48, {'sad_pepe_compilation.gif', 'grumpy_cat.gif', 'rollsafe.jpg', 'happy_pepe_compilation.gif', 'guitar.jpg'})
```

## Running the tests

Run tests.py

## Task requirements

* Each meme is used only once
* Function take exactly 2 arguments _usb_size_ and _memes_
* Function _calculate_ is in file _main.py_

## Authors

* **Jakub Zgrzebnicki** - [zgrzebnickij](https://github.com/zgrzebnickij)

