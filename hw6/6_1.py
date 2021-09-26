import sys


def add_sales(sum):
    with open('bakerySales.csv', 'a', encoding='utf-8') as f:
        f.write(f'{float(sum):.2f}\n')


add_sales(sys.argv[1])


