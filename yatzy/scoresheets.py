class YatzyScoresheet:
    def score_ones(self, hand):
        return sum(hand.ones)

    def score_twos(self, hand):
        return sum(hand.twos)

    def score_threes(self, hand):
        return sum(hand.threes)

    def score_fours(self, hand):
        return sum(hand.fours)

    def score_fives(self, hand):
        return sum(hand.fives)

    def score_sixes(self, hand):
        return sum(hand.sixes)

    def _score_set(self, hand, set_size):
        scores = [0]
        for worth, count in hand._sets.items():
            if count == set_size:
                scores.append(worth * set_size)
        return max(scores)

    def _score_straights(self, hand):
        check_straight = hand[0]
        scores = [0]
        for straight in hand[:5]:
            if straight == check_straight:
                scores.append(straight)
                check_straight += 1
        return sum(scores)

    def score_one_pair(self, hand,):
        return self._score_set(hand, 2)

    def score_two_pairs(self, hand, set_size=2):
        scores = [0]
        for worth, count in hand._sets.items():
            if count == set_size:
                scores.append(worth * set_size)
        return sum(scores)

    def score_small_straight(self, hand):
        return self._score_straights(hand)

    def score_large_straight(self, hand):
        return self._score_straights(hand)

    def score_four_of_a_kind(self, hand):
        return self._score_set(hand, 4)

    def score_three_of_a_kind(self, hand):
        return self._score_set(hand, 3)

    def score_chance(self, hand):
        return sum(hand)

    def score_full_house(self, hand):
        pair = self._score_set(hand, 2)
        three_of_a_king = self._score_set(hand, 3)
        return pair + three_of_a_king

    def score_yatzy(self, hand):
        first_die_value = hand[0]  # the value of the first die
        for current_die in hand:
            if current_die != first_die_value:
                return 0
        return 50
