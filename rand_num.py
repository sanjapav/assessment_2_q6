import numpy as np

class Ran_Number:

    def __init__(self, minRange, maxRange, amount):
        self.amount = int(amount)
        self.minRange = int(minRange)
        self.maxRange = int(maxRange)

    def rand_num(self):
        if self.minRange < 0:
            print("minRange must be equal to or larger than 0.")
        elif self.maxRange < self.minRange:
            print("maxRange must be bigger than minRange.")
        else:
            random_list = list(np.random.randint(low = self.minRange, high = self.maxRange, size = self.amount))
            print(random_list)

mytest = Ran_Number(1,10,5)
mytest.rand_num()