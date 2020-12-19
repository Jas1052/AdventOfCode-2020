def part1():
    file = open("input.txt", "r")
    index = 0
    LENGTH = 31
    treeCount = 0
    for line in file:
        if line[index] == '#':
            treeCount += 1
        index = (index + 3) % LENGTH
    print(treeCount)
    
def part2():
    slopes = [(1, 1), (3, 1), (5,1), (7,1), (1, 2)]
    treeCounts= []
    for tpl in slopes:
        file = open("input.txt", "r")
        index = 0
        LENGTH = 31
        treeCount = 0
        lineCount = 0
        prevLineCount = -1
        for line in file:
            lineCount+= 1
            if tpl[1] > 1:
                if lineCount < prevLineCount+tpl[1]:
                    continue
            if line[index] == '#':
                treeCount += 1
            index = (index + tpl[0]) % LENGTH
            prevLineCount = lineCount
        treeCounts.append(treeCount)
    total = 1
    for i in treeCounts:
        total *= i
    print(total)
        
        

if __name__ == "__main__":
    #part1()
    part2()