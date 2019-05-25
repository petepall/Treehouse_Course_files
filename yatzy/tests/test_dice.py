import unittest

from dice import Die, D6


class DiceTests(unittest.TestCase):
    def test_die(self):
        die = Die()
        self.assertIn(int(die), range(1, 3))

    def test_die_value(self):
        die = Die(value=8)
        self.assertEqual(int(die), 8)

    def test_d6(self):
        die = D6()
        self.assertEqual(die.sides, 6)

    def test_d6_value(self):
        die = D6()
        self.assertLessEqual(int(die), 6)
