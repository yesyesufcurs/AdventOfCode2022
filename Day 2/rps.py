score = 0

f = open("input.txt", "r")
mapper = {"X" : "r", "Y" : "p", "Z" : "s", "A" : "r", "B" : "p", "C" : "s", }
scoreMap = {"r" : 1, "p": 2, "s": 3}

for l in f.readlines():
    line = l.strip().split()
    if mapper[line[0]] == mapper[line[1]]:
        score += 3
    elif mapper[line[0]] == "s" and mapper[line[1]] == "r" or mapper[line[0]] == "r" and mapper[line[1]] == "p" or mapper[line[0]] == "p" and mapper[line[1]] == "s":
        score += 6
    
    score += scoreMap[mapper[line[1]]]

print(score)
    


