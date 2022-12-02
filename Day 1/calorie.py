max_cal = 0
curr_cal = 0

f = open("input.txt", "r")

for line in f.readlines():
    line = line.strip()
    if line == "":
        max_cal = max(max_cal, curr_cal)
        curr_cal = 0
    else:
        curr_cal += int(line)

print(max_cal)