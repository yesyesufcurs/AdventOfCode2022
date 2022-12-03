max_cal = 0
max_cal2 = 0
max_cal3 = 0
curr_cal = 0

f = open("input.txt", "r")

for line in f.readlines():
    line = line.strip()
    if line == "":
        # If curr_cal > max_cal: shift down max_cal to max_cal2 and max_cal2 to max_cal 3
        # etc etc.
        if curr_cal > max_cal:
            temp = max_cal2
            max_cal2 = max_cal
            max_cal3 = temp
            max_cal = curr_cal
        elif curr_cal > max_cal2:
            max_cal3 = max_cal2
            max_cal2 = curr_cal
        elif curr_cal > max_cal3:
            max_cal3 = curr_cal
        curr_cal = 0
    else:
        # if current line not empty, count calories
        curr_cal += int(line)

print("Maximum calories", max_cal)
print("Sum top 3", max_cal + max_cal2 + max_cal3)