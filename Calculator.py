import unittest

def percentage(num1, num2):
    if num2 > num1 and num1 > 0 and num2 > 0:
        return num1 / num2 * 100
    else:
        return -1

class TestPercentage(unittest.TestCase):
    def test_percentage_valid_input(self):
        self.assertEqual(percentage(10, 20), 50)

    def test_percentage_num2_less_than_num1(self):
        self.assertEqual(percentage(20, 10), -1)

    def test_percentage_num1_or_num2_zero(self):
        self.assertEqual(percentage(0, 10), -1)
        self.assertEqual(percentage(10, 0), -1)

if __name__ == '__main__':
    unittest.main()

