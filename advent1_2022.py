
def ReadFile(fileName):
    file = open(fileName, "r")
    lines = file.readlines()
    elves = []
    prevElfCal = 0
    currElfCal = 0
    top3ElfCal = 0

    for line in lines:
        readLine = line.strip()
        if readLine == "":
            elves.append(currElfCal)
            if currElfCal >= prevElfCal:
                prevElfCal = currElfCal
            currElfCal = 0
        else:
            currElfCal += int(readLine)

    elves.sort(reverse=True)
    for i in range(3):
        top3ElfCal += elves[i]


    return prevElfCal, top3ElfCal


def main():
    calories = ReadFile("calories.txt")
    print(calories[0], calories[1])


main()
