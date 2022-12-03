score_p1 = 0
score_p2 = 0

f = open("input.txt", "r")
mapper = {"X" : "r", "Y" : "p", "Z" : "s", "A" : "r", "B" : "p", "C" : "s", }
scoreMap = {"r" : 1, "p": 2, "s": 3}

for l in f.readlines():
    line = l.strip().split()
    opponent_play = mapper[line[0]]
    i_play = mapper[line[1]]
    if opponent_play == i_play:
        score_p1 += 3
    elif opponent_play == "s" and i_play == "r" or opponent_play == "r" and i_play == "p" or opponent_play == "p" and i_play == "s":
        score_p1 += 6
    
    score_p1 += scoreMap[i_play]

    if line[1] == "X":
        match opponent_play:
            case "r":
                score_p2 += scoreMap["s"]
            case "p":
                score_p2 += scoreMap["r"]
            case "s":
                score_p2 += scoreMap["p"]
    elif line[1] == "Y":
        score_p2 += 3 + scoreMap[opponent_play]
    else:
        score_p2 += 6
        match opponent_play:
            case "r":
                score_p2 += scoreMap["p"]
            case "p":
                score_p2 += scoreMap["s"]
            case "s":
                score_p2 += scoreMap["r"]

print(score_p1)
print(score_p2)
    


