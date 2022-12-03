
def getContents(line):
    size = int(len(line)/2)
    return [line[:size],line[-size:]]

def intersection(contents):
    return list(set.intersection(*[set(list(c)) for c in contents]))

def priority(i):
    o = ord(i[0])
    if o > 90: #lowercase
        return o-96
    return o-38

if __name__ == "__main__":
    with open('input.txt','r') as input:
        lines = [line.rstrip() for line in input]

    intersections = [intersection(getContents(l)) for l in lines]
    groups = [lines[i:i+3] for i in range(0,len(lines),3)]
    badges = [intersection(g) for g in groups]
    totalbadges = sum([priority(b) for b in badges])
    totalpriority = sum([priority(i) for i in intersections])
    print(f"All priorities:{totalpriority}, badges: {totalbadges}")
