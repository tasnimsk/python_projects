from random import sample
from pprint import pprint

#generating the sudoku grid 

base = 3
side = base * base
row_base = range(base)

def shuffle(side):
    return sample(side,len(side))

def pattern(row, column):
    return (base * (row % base) + row // base + column) % side

rows = [g * base + row for g in shuffle(row_base) for row in shuffle(row_base)]
columns = [g * base + column for g in shuffle(row_base) for column in shuffle(row_base)]
nums = shuffle(range(1, base * base + 1))

grid = [[nums[pattern(row, column)] for column in columns] for row in rows]

pprint(grid)