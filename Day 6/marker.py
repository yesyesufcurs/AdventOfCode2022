f = open("input.txt", "r")

line = f.readline()

def find_marker(size):
    for i in range(size, len(line)):
        testedString = line[i - size:i]
        if len(set(testedString)) == len(testedString):
            print(i)
            break

find_marker(4)
find_marker(14)