import unittest
import sys

def find_median(num1, num2, num3):
    numbers = [num1, num2, num3]
    numbers.sort()
    return numbers[1]

class TestFindMedian(unittest.TestCase):
    def test_median_three_numbers(self):
        self.assertEqual(find_median(1, 2, 3), 2)
        self.assertEqual(find_median(3, 2, 1), 1) # this test fails
        self.assertEqual(find_median(2, 3, 1), 2)

def guessing_game():
    answer = 42
    guess = int(input("Guess a number between 1 and 100: "))
    while guess != answer:
        if guess < answer:
            print("Too low")
        else:
            print("Too high")
        guess = int(input("Guess again: "))
    print("You got it!")
    sys.exit(0)

class TestGuessingGame(unittest.TestCase):
    def test_guess_correct(self):
        with self.assertRaises(SystemExit) as cm:
            guessing_game()
        self.assertEqual(cm.exception.code, 0)

if __name__ == '__main__':
    unittest.main()

