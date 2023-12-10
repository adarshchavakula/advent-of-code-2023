# read input file

with open('./day1.txt') as f:
    data = f.readlines()

# Part 1

all_sum = 0
for line in data:
    num = ''
    for c in line:
        if c.isnumeric():
            num += c
    actual_num = num[0] + num[-1]
    all_sum += int(actual_num)

print(f"First part answer: {all_sum}")

# Part 2

def insert_num_to_str(s):
    """
    insert number into their corresponding words after first letter
    eg: two --> t2wo

    """
    vals = {
        'one': '1', 
        'two': '2', 
        'three': '3', 
        'four': '4', 
        'five': '5', 
        'six': '6', 
        'seven': '7', 
        'eight': '8',
        'nine': '9'
    }
    for k, v in vals.items():
        s = s.replace(k, k[0] + v + k[1:])
    return s

# testcase
assert(insert_num_to_str("eightwothree") == "e8ight2wot3hree")

all_sum = 0
for line in data:

    num = ''
    for c in insert_num_to_str(line):
        if c.isnumeric():
            num += c
    actual_num = num[0] + num[-1]
    all_sum += int(actual_num)
print(f"Second part answer: {all_sum}")

