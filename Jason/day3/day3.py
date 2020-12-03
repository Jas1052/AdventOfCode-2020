rows = []
with open('input.txt') as f:
    for row in f:
        rows.append(row)
tree = '#'
x = 0
hit = 0

even = 0
for row in rows:
    even += 1
    if even % 2 == 0:
        continue
    if row[x] == tree:
        hit += 1
    x = (x + 1) % (len(row) - 1)

print(hit)
# 38
# 67
# 299
# 67
# 71
print(38 * 67 * 299 * 67 * 71)