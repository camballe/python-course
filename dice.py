import random


class Dice:
    def roll(self):
        values = (random.randint(1, 6), random.randint(1, 6))
        print(values)


dice1 = Dice()
dice1.roll()
