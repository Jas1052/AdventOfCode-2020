# just realized i don't need this at all, i can just convert to binary
def binary(lower, upper, direction):
    if direction == 0:
        return lower, (upper + lower) // 2
    return ((upper + lower) // 2) + 1, upper


def get_seat(tag):
    row_vals = tag[0:7]
    col_vals = tag[7:10]

    row_val = 0, 127
    for letter in row_vals:
        row_val = binary(row_val[0], row_val[1], 0 if letter == "F" else 1)
    row_val = row_val[0]

    col_val = 0, 7
    for letter in col_vals:
        col_val = binary(col_val[0], col_val[1], 0 if letter == "L" else 1)
    col_val = col_val[0]

    return row_val, col_val


seats = []
biggest_seat = -1
with open('input.txt') as f:
    for row in f:
        seat = get_seat(row)
        seat = seat[0] * 8 + seat[1]
        seats.append(seat)
        if seat > biggest_seat:
            biggest_seat = seat

for i in range(1024):
    if not seats.__contains__(i):
        print(i)

# 890
print(biggest_seat)

# 651
