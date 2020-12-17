#Part 1
def part1 ():
    file = open("input.txt", "r")
    sumTrack = set()
    sumTrack.add(int(file.readline()))
    TARGET = 2020
    for line in file:
        match = TARGET - int(line)
        if match in sumTrack:
            print(int(line) * match)
            exit(0)
        sumTrack.add(int(line))

def part2():
    file = open("input.txt", "r")
    file2 = open("input.txt", "r")
    sumTrack = {}
    TARGET = 2020
    for line in file:
        file2 = open("input.txt", "r")
        for line2 in file2:
            sum = int(line2)+int(line)
            if sum < TARGET:
                sumTrack[sum] = (int(line2), int(line))
    file = open("input.txt", "r")
    for line in file:
        match = TARGET - int(line)
        if match in sumTrack:
            print(int(line)*sumTrack[match][0]*sumTrack[match][1])
            exit(0)
        
if __name__ == "__main__":
    #part1()
    part2()
    

