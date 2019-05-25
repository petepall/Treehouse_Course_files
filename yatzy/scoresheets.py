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

    def score_one_pair(self, hand):
        return self._score_set(hand, 2)

    def score_two_pairs(self, hand):
        pass

    def score_chance(self, hand):
        return sum(hand)

    def score_yatzy(self, hand):
        first_die_value = hand[0]  # the value of the first die
        for current_die in hand:
            if current_die != first_die_value:
                return 0
        return 50
