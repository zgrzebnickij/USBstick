import unittest
from main import calculate, brute


class TestExampleData(unittest.TestCase):

    def test_dynamic_example_data(self):
        usb_size = 1
        memes = [
            ('rollsafe.jpg', 205, 6),
            ('sad_pepe_compilation.gif', 410, 10),
            ('yodeling.avi', 605, 12)
        ]

        results = calculate(usb_size, memes)
        print(results)
        assert((22, {'sad_pepe_compilation.gif', 'yodeling.avi'}) == results)

    def test_brute_force_example_data(self):
        usb_size = 1
        memes = [
            ('rollsafe.jpg', 205, 6),
            ('sad_pepe_compilation.gif', 410, 10),
            ('yodeling.avi', 605, 12)
        ]
        result = brute(usb_size, memes)
        print(result)
        assert(result == (22, {'sad_pepe_compilation.gif', 'yodeling.avi'}))

    def test_brute_force_equale_to_dynamic(self):
        usb_size = 1
        memes = [
            ('rollsafe.jpg', 205, 6),
            ('sad_pepe_compilation.gif', 410, 10),
            ('yodeling.avi', 605, 12),
            ('pepe.jpg', 105, 3),
            ('cat.gif', 302, 20),
            ('kid.avi', 800, 11),
            ('guitar.jpg', 90, 2),
            ('happy_pepe_compilation.gif', 12, 10),
            ('kill.avi', 890, 13)
        ]
        br = brute(usb_size, memes)
        cal = calculate(usb_size, memes)
        print(br, cal)
        assert(br == cal)

