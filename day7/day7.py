#part1 1086293
#part2 366028

class File:
    def __init__(self, name, size, parent):
        self.name = name
        self._size = int(size)
        self.parent = parent

    def __str__(self):
        return f"{self.size} : {self.name}"

    def size(self):
        return self._size


class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.children = []
        self.parent = parent
        self._size = -1

    def add_child(self,child):
        self.children.append(child)

    def get_child_named(self, name):
        return [c for c in self.children if c.name == name][0]

    def __str__(self):
        return f"dir {self.name}"

    def size(self):
        if self._size == -1:
            self._size = sum([c.size() for c in self.children])
        return self._size


if __name__ == "__main__":
    root = Directory("/", None)
    allDirs = [root]
    currentDir = root
    with open("input.txt",'r') as input:
        firstline = input.readline()
        if firstline.rstrip() != "$ cd /":
            print("Bad input!")
            exit(1)
        secondline = input.readline()
        if secondline.rstrip() != "$ ls":
            print("Bad input!")
            exit(1)

        allDirs = []

        for line in input:
            line = line.rstrip()
            if line.startswith("$"):
                # going into a command
                if line.startswith("$ cd"):
                    cddir = line.split()[2]
                    if(cddir == ".."):
                        currentDir = currentDir.parent
                    else:
                        currentDir = currentDir.get_child_named(cddir)
                elif line != "$ ls":
                    print("Bad input?")
                    exit(1)
            else:
                if line.startswith("dir"):
                    dirname = line.split()[1]
                    new_dir = Directory(dirname, currentDir)
                    allDirs.append(new_dir)
                    currentDir.add_child(new_dir)
                else:
                    (size,name) = line.split()
                    currentDir.add_child(File(name,size, currentDir))

    #part one
    matches = [d.size() for d in allDirs if d.size() <= 100000]
    print(f"Part 1: {sum(matches)}")

    #part two
    total_used = root.size()
    unused = 70000000 - total_used
    needed = 30000000 - unused
    target = min([d.size() for d in allDirs if d.size() >= needed])
    print(f"Part 2: {target}")
