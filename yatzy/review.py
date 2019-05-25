from hands import YatzyHand
from dice import D6
from scoresheets import YatzyScoresheet


def main():
    hand = YatzyHand()
    three = D6(value=3)
    four = D6(value=4)
    one = D6(value=1)
    hand[:] = [one, three, three, four, four]
    print(YatzyScoresheet().score_one_pair(hand))


if __name__ == "__main__":
    main()
