import re
text = ""

with open('input.txt') as f:
    for row in f:
        text = text + row

req_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
valid = 0
passports = text.split('\n\n')

field_conditions = {'byr': lambda val: 1920 <= int(val) <= 2002,
                    'iyr': lambda val: 2010 <= int(val) <= 2020,
                    'eyr': lambda val: 2020 <= int(val) <= 2030,
                    'hgt': lambda val: re.search('^(((1[5-8][0-9]|19[0-3])cm)|((59|6[0-9]|7[0-6])in))$', val),
                    'hcl': lambda val: re.search('^#([a-f]|[0-9]){6}$', val),
                    'ecl': lambda val: val in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
                    'pid': lambda val: re.search('^[0-9]{9}$', val)}


for passport in passports:
    fields_breakdown = re.split(' |\n', passport)
    count = 0
    for field in fields_breakdown:
        field = field.split(':')
        if field[0] in field_conditions and field_conditions[field[0]](field[1]):
            count += 1
    if count == len(req_fields):
        valid += 1

# 133
print(valid)
