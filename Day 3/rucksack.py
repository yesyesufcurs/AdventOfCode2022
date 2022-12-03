letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Given the letter, return its priority.
def priority(letter):
    return 1 + letters.index(letter)


f = open("input.txt", "r")

sum_of_prio = 0
sum_of_group = 0
count = 0

prev_line = ""
prev_prev_line = ""

for line in f.readlines():
    count += 1

    line = line.strip()
    nr_items = len(line)
    compartment1 = line[:nr_items // 2]
    compartment2 = line[nr_items // 2:]
    # Look for an item that is in both compartments
    for item in compartment1:
        if item in compartment2:
            sum_of_prio += priority(item)
            break
    
    # If count is a multiple of 3, we have a new group, look for its badge
    if count % 3 == 0:
        for item in line:
            if item in prev_line and item in prev_prev_line:
                sum_of_group += priority(item)
                break
    # Else save the previous lines.
    else:
        prev_prev_line = prev_line
        prev_line = line

print(sum_of_prio)

print(sum_of_group)