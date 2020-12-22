def part1():
    file = open("input.txt", "r")
    validCount = 0
    currentEntry = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
    for line in file:
        if not line.strip():
            if len(currentEntry) == 0 or currentEntry[0] == "cid":
                validCount += 1
            currentEntry = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]         
        else:
            arr = line.split(' ')
            for item in arr:
                label = item.split(":")
                currentEntry.remove(label[0])
    if len(currentEntry) == 0 or currentEntry[0] == "cid":
        validCount += 1
    print(validCount)

def part2():
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    # hgt (Height) - a number followed by either cm or in:
    #     If cm, the number must be at least 150 and at most 193.
    #     If in, the number must be at least 59 and at most 76.
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    # cid (Country ID) - ignored, missing or not.
    file = open("input.txt", "r")
    validCount = 0
    currentEntry = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
    for line in file:
        if not line.strip():
            if len(currentEntry) == 0 or currentEntry[0] == "cid":
                validCount += 1
            currentEntry = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]         
        else:
            arr = line.split(' ')
            for item in arr:
                lbl, val = item.split(":")
                if lbl == "byr":
                    if int(val) < 1920 or int(val) > 2002 or len(val.strip()) != 4:
                        continue
                elif lbl == "iyr":
                    if int(val) < 2010 or int(val) > 2020 or len(val.strip()) != 4:
                        continue 
                elif lbl == "eyr":
                    if int(val) < 2020 or int(val) > 2030 or len(val.strip()) != 4:
                        continue 
                elif lbl == "hgt":
                    val = str(val).strip()
                    i = 0
                    while val[i].isdigit():
                        i += 1
                        if i == len(val):
                            break
                    if i == len(val):
                        continue
                    hgt = val[0:i]
                    unit = val[i:].strip()
                    if unit == 'cm':
                        if int(hgt) < 150 or int(hgt) > 193:
                            continue 
                    elif unit == 'in':
                        if int(hgt) < 59 or int(hgt) > 76:
                           continue 
                elif lbl == "hcl":
                    val = str(val).strip()
                    hexLetters = ['0', '1','2', '3', '4', '5', '6', '7', '8', '9','a', 'b', 'c', 'd', 'e', 'f']
                    if val[0] != '#' or len(val) > 7:
                        continue
                    i =1
                    failed = False
                    while i < len(val):
                        if not val[i] in hexLetters:
                            failed = True
                            break
                        i += 1
                    if failed:
                        continue
                elif lbl == "ecl":
                    val = str(val).strip()
                    validColors =  ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                    if not val in validColors:
                        continue
                elif lbl == "pid":
                    val = str(val).strip()
                    if len(val) != 9 or not val.isnumeric():
                        continue
                currentEntry.remove(lbl)
    if len(currentEntry) == 0 or currentEntry[0] == "cid":
        validCount += 1
    print(validCount)



if __name__ == "__main__":
    part2()