import unittest
from main import calculate, brute


class TestExampleData(unittest.TestCase):

    def test_calculate_example1_data(self):
        usb_size = 1
        memes = [
            ('rollsafe.jpg', 205, 6),
            ('sad_pepe_compilation.gif', 410, 10),
            ('yodeling.avi', 605, 12)
        ]

        results = calculate(usb_size, memes)
        self.assertEqual((22, {'sad_pepe_compilation.gif', 'yodeling.avi'}),
                         results,
                         "Calculate function do not pass example 1")

    def test_brute_force_example1_data(self):
        usb_size = 1
        memes = [
            ('rollsafe.jpg', 205, 6),
            ('sad_pepe_compilation.gif', 410, 10),
            ('yodeling.avi', 605, 12)
        ]
        result = brute(usb_size, memes)
        self.assertEqual(result,
                         (22, {'sad_pepe_compilation.gif', 'yodeling.avi'}),
                         "Brute force function do not pass example 1")

    def test_brute_force_equal_to_calculate_example2_data_with_only_one_answer(self):
        usb_size = 1
        # for this list of memes there is only one solution
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
        calculate_result = calculate(usb_size, memes)
        print(calculate_result)
        self.assertEqual(calculate_result,
                         (48, {'guitar.jpg', 'grumpy_cat.gif', 'sad_pepe_compilation.gif',
                               'happy_pepe_compilation.gif', 'rollsafe.jpg'}),
                         "Dynamic and brute force solutions have different results")

    def test_calculate_for_empty_memes_list(self):
        usb_size = 1
        memes = []
        results = calculate(usb_size, memes)
        self.assertEqual((0, frozenset()),
                         results,
                         "Calculate function do not return empty set")

    def test_calculate_for_zero_capacity(self):
        usb_size = 0
        memes = [
            ('rollsafe.jpg', 205, 6),
            ('sad_pepe_compilation.gif', 410, 10),
            ('yodeling.avi', 605, 12)
        ]
        results = calculate(usb_size, memes)
        self.assertEqual((0, frozenset()),
                         results,
                         "Calculate function do not return empty set")


if __name__ == '__main__':
    unittest.main()
