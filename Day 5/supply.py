stacks = [[] for _ in range(9)]
stacks2 = [[] for _ in range(9)]
f = open("input.txt", "r")

reading = True
for line in f.readlines():
    # Read in stacks
    if reading and line[:2] != " 1":
        for i in range(len(line)):
            if line[i].isalpha():
                stacks[i // 4].insert(0, line[i])
                stacks2[i // 4].insert(0, line[i])
    else:
        reading = False

    if line[0] == "m":

        # Get number of moves, from position, to position
        number, source, target = [int(x) for x in line.split() if x.isdigit()]
        # part 1
        for _ in range(number):
            element = stacks[source - 1].pop()
            stacks[target - 1].append(element)
        
        # part 2
        elements = []
        for _ in range(number):
            elements.append(stacks2[source - 1].pop())
        for i in range(number - 1, -1, -1):
            stacks2[target - 1].append(elements[i])

string = ""
string2 = ""
for stack in stacks:
    string += stack[-1]
for stack in stacks2:
    string2 += stack[-1]
print(string)
print(string2)
    
