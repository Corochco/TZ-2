import unittest

from set_Up_file import *
from main import Main
from matplotlib import pyplot as plt
from datetime import *



class TestMain(unittest.TestCase):
    last = 0

    def setUp(self) -> None:
        self.begin = datetime.now()
        self.Main = Main()

    def tearDown(self) -> None:
        self.end = datetime.now()
        diff = self.end - self.begin
        last = diff.microseconds / 1000

    def test_min(self, n=1000000):
        file_set_Up(n)
        self.Main = Main()
        f = open('input.txt')
        minimal = min(list(map(int, f.readline().split())))
        f.close()
        self.assertEqual(minimal, self.Main._min())

    def test_max(self, n=1000000):
        file_set_Up(n)
        self.Main = Main()
        f = open('input.txt')
        maximal = max(list(map(int, f.readline().split())))
        f.close()
        self.assertEqual(maximal, self.Main._max())

    def test_sum(self, n=1000000):
        file_set_Up(n)
        self.Main = Main()
        f = open('input.txt')
        summa = sum(list(map(int, f.readline().split())))
        f.close()
        self.assertEqual(summa, self.Main._sum())

    def test_mult(self, n=1000000):
        file_set_Up(n)
        self.Main = Main()
        f = open('input.txt')
        lst = list(map(int, f.readline().split()))
        f.close()
        counter = 1
        for i in lst:
            counter *= i
        self.assertEqual(counter, self.Main._mult())

    def test_min_graph(self):
        array = []
        lst = []
        for i in range(1, 1000000, 100000):
            length = i
            f = open('input.txt')
            file_set_Up(i)
            main1 = Main()
            f.close()
            begin = datetime.now()
            main1._min()
            end = datetime.now()
            array.append((end - begin).microseconds / 1000)
            lst.append(length)
        plt.plot(lst, array)
        plt.title('Tests _min')
        plt.ylabel('Time in ms')
        plt.xlabel('Count of numbers')
        plt.show()

    def test_max_graph(self):
        array = []
        lst = []
        for i in range(1, 1000000, 100000):
            length = i
            f = open('input.txt')
            file_set_Up(i)
            main1 = Main()
            f.close()
            begin = datetime.now()
            main1._max()
            end = datetime.now()
            array.append((end - begin).microseconds / 1000)
            lst.append(length)
        plt.plot(lst, array)
        plt.title('Tests _max')
        plt.ylabel('Time in ms')
        plt.xlabel('Count of numbers')
        plt.show()

    def test_sum_graph(self):
        array = []
        lst = []
        for i in range(1, 1000000, 100000):
            length = i
            f = open('input.txt')
            file_set_Up(i)
            main1 = Main()
            f.close()
            begin = datetime.now()
            main1._sum()
            end = datetime.now()
            array.append((end - begin).microseconds / 1000)
            lst.append(length)
        plt.plot(lst, array)
        plt.title('Tests _sum')
        plt.ylabel('Time in ms')
        plt.xlabel('Count of numbers')
        plt.show()

    def test_mult_graph(self):
        array = []
        lst = []
        for i in range(1, 1000000, 100000):
            length = i
            f = open('input.txt')
            file_set_Up(i)
            main1 = Main()
            f.close()
            begin = datetime.now()
            main1._mult()
            end = datetime.now()
            array.append((end - begin).microseconds / 1000)
            lst.append(length)
        plt.plot(lst, array)
        plt.title('Tests _mult')
        plt.ylabel('Time in ms')
        plt.xlabel('Count of numbers')
        plt.show()
