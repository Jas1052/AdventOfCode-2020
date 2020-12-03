target = 2020
rows = []
with open('input.txt') as f:
    for row in f:
        rows.append(row)

valid = 0
valid2 = 0
for row in rows:
    sections = row.split(' ')
    lower = int(sections[0].split('-')[0])
    upper = int(sections[0].split('-')[1])
    letter = sections[1][0]
    text = sections[2]

    # p1
    num = text.count(letter)
    if upper >= num >= lower:
        valid += 1

    # p2
    lower_match = (lower - 1 < len(text) and text[lower - 1] == letter)
    upper_match = (upper - 1 < len(text) and text[upper - 1] == letter)
    if (lower_match or upper_match) and not (lower_match and upper_match):
        valid2 += 1

print(valid)
# 564

print(valid2)
# 325
