#part 1 = 1715
#part 2 = 374400
import numpy as np
from functools import reduce
from operator import mul


def num_visible_trees(row, spotrow):
    count = 1 if not spotrow[0] else 0
    spotrow[0] = True
    max = row[0]
    for tree in range(1,len(row)):
        if row[tree] > max:
            count+= 1 if not spotrow[tree] else 0
            spotrow[tree] = True
            max = row[tree]
    return count

def sightline(x, y, direction,trees):
    visible = 0
    max = trees[x, y]
    (x, y) = (x+direction[0], y+direction[1])
    while 0 <= x < trees.shape[0] and 0 <= y < trees.shape[1]:
        tree = trees[x, y]
        if tree < max:
            visible += 1
        else:
            visible += 1
            return visible
        (x, y) = (x + direction[0], y + direction[1])
    return visible

if __name__ == "__main__":
    with open("input.txt",'r') as input:
        trees = np.array([ [int(t) for t in list(line.rstrip())] for line in input ])
        spotted = np.zeros(trees.shape, dtype=np.bool)
    total = 0
    maxtree = 0
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)] # N W E S
    for x in range(trees.shape[0]):
        for y in range(trees.shape[1]):
            sightlines = []
            for axis in range(4):
                sightlines.append(sightline(x, y, directions[axis], trees))
            maxtree = max(maxtree, reduce(mul, sightlines, 1))

    print(maxtree)

