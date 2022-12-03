
if __name__ == "__main__":
    groups = []
    linesRead = 0
    with open('input.txt','r') as input:
        total = 0
        while True:
            line = input.readline()
            linesRead += 1
            try:
                total += int(line)
            except ValueError as e:
                groups.append(total)
                total = 0
            if line == "":
                break

    print(f"Top Three: {sum(sorted(groups)[-3:])}, linesRead: {linesRead}")

