# https://justjoin.it/offers/reef-technologies-senior-python-backend-engineer
# https://careers.reef.pl/
# https://evalground.com/
import sys
import csv

def print_reverse_order(lines):
    reversed = lambda x: x[::-1]
    # print out input from stdin in reverse order
    for line in reversed(lines):
        print(reversed(line.rstrip()))

def swap_csv_columns(lines):
    # print out input from stdin with 2nd and 3rd columns always swapped
    reader = csv.reader(lines)
    for row in reader:
        print(row[0], row[2], row[1], *row[3:])

if __name__ == '__main__':
    lines = sys.stdin.readlines()
    swap_csv_columns(lines)