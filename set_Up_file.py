import random


def file_set_Up(high):
    s = ''
    for i in range(high):
        s += str(random.randint(1, 10000)) + ' '
    s = s[0:-1]
    with open('input.txt', 'w') as f:
        f.write(s)
    with open('all_tests.txt', 'a+') as f:
        f.write(s + '\n')
