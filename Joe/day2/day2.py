def part1():
    input = open("input.txt", "r")
    valid = 0
    for line in input:
        lower = ""
        upper = ""
        letter = ""
        count = 0
        i = 0
        while line[i] != '-':
            lower+=line[i]
            i+=1
        lower = int(lower)
        i+= 1
        while line[i] != ' ':
            upper+=line[i]
            i+=1
        upper = int(upper)
        i += 1
        letter = line[i]
        i+=2
        while i < len(line):
            if line[i] == letter:
                count+= 1
            i += 1
        if count <= upper and count >= lower:
            valid+=1
    print(valid)

def part2():
    input = open("input.txt", "r")
    valid = 0
    for line in input:
        lower = ""
        upper = ""
        letter = ""
        count = 0
        i = 0
        while line[i] != '-':
            lower+=line[i]
            i+=1
        lower = int(lower) -1
        i+= 1
        while line[i] != ' ':
            upper+=line[i]
            i+=1
        upper = int(upper) -1 
        i += 1
        letter = line[i]
        i+=3
        if line[i+lower] == letter:
            count+=1
        if line[i+upper] == letter:
            count+=1
        if count == 1:
            valid +=1
    print(valid)

            

if __name__ == "__main__":
    #part1()
    part2()