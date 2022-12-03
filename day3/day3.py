
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
    with open('testinput.txt','r') as input:
        intersections = [intersection(getContents(line.rstrip())) for line in input]

    print(sum([priority(i) for i in intersections]))