class Main:
    def __init__(self):
        with open('input.txt') as f:
            self.array = list(map(int, f.readline().split()))

    def _min(self):
        minimal = 10000000
        for i in self.array:
            if i < minimal:
                minimal = i
        return minimal

    def _max(self):
        maximal = -10000000
        for i in self.array:
            if i > maximal:
                maximal = i
        return max(self.array)

    def _sum(self):
        summa = 0
        for i in self.array:
            summa += i
        return sum(self.array)

    def _mult(self):
        counter = 1
        for i in self.array:
            counter *= i
        return counter
