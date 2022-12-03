
if __name__ == "__main__":
    grouping = 0
    maxGroup = -1
    maxCalories = -1
    linesRead = 0
    with open('input.txt','r') as input:
        total = 0
        while True:
            line = input.readline()
            linesRead += 1
            try:
                total += int(line)
            except ValueError as e:
                maxCalories = max(maxCalories,total)
                if maxCalories == total:
                    maxGroup = grouping
                grouping += 1
                total = 0
            if line == "":
                break

    print(f"Group: {grouping}, calories: {maxCalories}, linesRead: {linesRead}")

