import random


class Die:
    def __init__(self, sides=2, value=0):
        if not sides >= 2:
            raise ValueError("Must have at lease 2 sides")
        if not isinstance(sides, int):
            raise ValueError("Sides must be a whole number")
        self.value = value or random.randint(1, sides)


class D6(Die):
    def __init__(self, sides=2, value=0):
        return super().__init__(sides=6, value=value)


d = Die()
print(d.value)

d6 = D6()
print(d6.value)
