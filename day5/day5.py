# TLFGBZHCN for part 1
# QRQFHFWCL for part 2

def move(crates, num, source , dest):
    stack = [crates[source].pop() for m in range(num)]
    stack.reverse()
    [crates[dest].append(m) for m in stack]

if __name__ == "__main__":
    with open("input.txt",'r') as input:
        lines = [line for line in input]
        num_columns = int((len(lines[0]) + 1) / 4)
        crates = [[] for a in range(num_columns)]

        for l in range(len(lines)):
            if lines[l].rstrip() == "":
                preamble = l - 1
                moves = l + 1
                break

        cratetext = lines[:preamble]
        movetext = lines[moves::]
        for line in cratetext:
            letters = [i for i in line[1::4]]
            for l in range(num_columns):
                ll = letters[l]
                if ll != " ":
                    crates[l].append(ll)

        for c in crates:
            c.reverse()

        for line in movetext:
            split = line.split(' ')
            (num, source, dest) = int(split[1]), int(split[3]) -1 , int(split[5]) -1
            move(crates, num, source,dest)

    tops = "".join([c[-1] for c in crates])
    print(tops)