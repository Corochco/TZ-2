import random


def file_set_Up(high):
    s = ''
    for i in range(high):
        s += str(random.randint(-10000, 10000)) + ' '
    s = s[0:-1]
    with open('input.txt', 'w') as f:
        f.write(s)
