import sys


def show_sales(start=1, stop=10000):
    with open('bakerySales.csv', 'r', encoding='utf-8') as f:
        h = f.read().split('\n')
        # print(f.readlines(n))
        print(h[start - 1: stop])

show_sales(2, 6)