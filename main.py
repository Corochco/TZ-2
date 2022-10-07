class Main:
    def __init__(self):
        with open('input.txt') as f:
            self.array = list(map(int, f.readline().split()))

    def _min(self):
        return min(self.array)

    def _max(self):
        return max(self.array)

    def _sum(self):
        return sum(self.array)

    def _mult(self):
        counter = 1
        for i in self.array:
            counter *= i
        return counter
