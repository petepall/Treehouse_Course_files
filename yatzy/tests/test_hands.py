import unittest

# import yatzy.dice as dice
from dice import D6
# import yatzy.hands as hands
from hands import Hand, YatzyHand
# import yatzy.scoresheets as scoresheets
from scoresheets import YatzyScoresheet


class DiceTests(unittest.TestCase):
    def setUp(self):
        self.dice = [D6(value=n) for n in range(1, 7)]

    def _seed(self, nums):
        return [D6(value=num) for num in nums]


class HandTests(DiceTests):
    def test_hand(self):
        hand = Hand(size=5, die_class=D6)
        self.assertEqual(len(hand), 5)

    def test_hand_sort(self):
        hand = Hand(size=5, die_class=D6)
        self.assertEqual(hand, sorted(hand))


class ScoresheetTests(DiceTests):
    def setUp(self):
        super().setUp()
        self.scoresheet = YatzyScoresheet()

    def test_ones(self):
        hand = YatzyHand()
        hand[:] = self.dice[:5]
        self.assertEqual(self.scoresheet.score_ones(hand), 1)

    def test_twos(self):
        hand = YatzyHand()
        hand[:] = self.dice[:5]
        self.assertEqual(self.scoresheet.score_twos(hand), 2)

    def test_threes(self):
        hand = YatzyHand()
        hand[:] = self.dice[:5]
        self.assertEqual(self.scoresheet.score_threes(hand), 3)

    def test_fours(self):
        hand = YatzyHand()
        hand[:] = self.dice[:5]
        self.assertEqual(self.scoresheet.score_fours(hand), 4)

    def test_fives(self):
        hand = YatzyHand()
        hand[:] = self.dice[:5]
        self.assertEqual(self.scoresheet.score_fives(hand), 5)

    def test_sixes(self):
        hand = YatzyHand()
        hand[:] = self.dice[1:]
        self.assertEqual(self.scoresheet.score_sixes(hand), 6)

    def test_one_pair(self):
        hand = YatzyHand()
        hand[:] = [self.dice[0], self.dice[0], self.dice[3]]
        self.assertEqual(self.scoresheet.score_one_pair(hand), 2)

    def test_one_pair_no_pairs(self):
        hand = YatzyHand()
        hand[:] = self.dice[:5]
        self.assertEqual(self.scoresheet.score_one_pair(hand), 0)

    def test_two_pairs(self):
        hand = YatzyHand()
        hand[:] = [self.dice[1], self.dice[0],
                   self.dice[0], self.dice[3], self.dice[3]]
        self.assertEqual(self.scoresheet.score_two_pairs(hand), 10)

    def test_two_pairs_no_pairs(self):
        hand = YatzyHand()
        hand[:] = self.dice[1:]
        self.assertEqual(self.scoresheet.score_two_pairs(hand), 0)

    def test_two_pairs_one_pair(self):
        hand = YatzyHand()
        hand[:] = [self.dice[0], self.dice[0], self.dice[3]]
        self.assertEqual(self.scoresheet.score_two_pairs(hand), 2)

    def test_three_of_a_kind(self):
        hand = YatzyHand()
        hand[:] = self._seed([2, 2, 2, 4, 5])
        self.assertEqual(self.scoresheet.score_three_of_a_kind(hand), 6)

    def test_four_of_a_kind(self):
        hand = YatzyHand()
        hand[:] = self._seed([2, 2, 2, 2, 5])
        self.assertEqual(self.scoresheet.score_four_of_a_kind(hand), 8)

    def test_yatzy(self):
        hand = YatzyHand()
        hand[:] = self._seed([2, 2, 2, 2, 2])
        self.assertEqual(self.scoresheet.score_yatzy(hand), 50)

    def test_small_straight(self):
        hand = YatzyHand()
        hand[:] = self.dice[:5]
        self.assertEqual(self.scoresheet.score_small_straight(hand), 15)

    def test_large_straight(self):
        hand = YatzyHand()
        hand[:] = self.dice[1:]
        self.assertEqual(self.scoresheet.score_large_straight(hand), 20)

    def test_full_house(self):
        hand = YatzyHand()
        hand[:] = self._seed([2, 2, 5, 5, 5])
        self.assertEqual(self.scoresheet.score_full_house(hand), 19)

    def test_chance(self):
        hand = YatzyHand()
        hand[:] = self._seed([4, 3, 3, 2, 1])
        self.assertEqual(self.scoresheet.score_chance(hand), 13)
