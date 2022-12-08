#part 1 = 1715

import numpy as np

def num_visible_trees(row,spotrow):
    count = 1 if not spotrow[0] else 0
    spotrow[0] = True
    max = row[0]
    for tree in range(1,len(row)):
        if row[tree] > max:
            count+= 1 if not spotrow[tree] else 0
            spotrow[tree] = True
            max = row[tree]
    return count


if __name__ == "__main__":
    with open("input.txt",'r') as input:
        trees = np.array([ [int(t) for t in list(line.rstrip())] for line in input ])
        spotted = np.zeros(trees.shape, dtype=np.bool)
    total = 0
    print(trees.shape)
    for i in range(4):
        for row in range(trees.shape[0]):
             total = total + num_visible_trees(trees[row], spotted[row])
        trees = np.rot90(trees)
        spotted = np.rot90(spotted)
    print(total)

