f = open("input.txt", "r")
grid : list[list['Tree']] = []

# Tree object, so we count each tree only once
class Tree:
    size : int
    def __init__(self, size) -> None:
        self.size = size

# Read grid

for line in f.readlines():
    line=line.strip()
    grid.append([Tree(int(size)) for size in line])

visibleTrees = set()

# Check visible trees from the left and right:
for i in range(len(grid)):
    highestTree = -1
    for j in range(len(grid[i])):
        if grid[i][j].size > highestTree:
            visibleTrees.add(grid[i][j])
            highestTree = grid[i][j].size
    
    highestTree = -1
    for j in range(len(grid[i]) - 1, -1, -1):
        if grid[i][j].size > highestTree:
            visibleTrees.add(grid[i][j])
            highestTree = grid[i][j].size

# Check visible trees from top and bottom

for i in range(len(grid)):
    highestTree = -1
    for j in range(len(grid[i])):
        if grid[j][i].size > highestTree:
            visibleTrees.add(grid[j][i])
            highestTree = grid[j][i].size
    
    highestTree = -1
    for j in range(len(grid[i]) - 1, -1, -1):
        if grid[j][i].size > highestTree:
            visibleTrees.add(grid[j][i])
            highestTree = grid[j][i].size

print(len(visibleTrees))


# Compute max scenic score
max_scene = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        visibilityLeft = 0
        
        for k in range(j - 1, -1, -1):
            visibilityLeft += 1
            if grid[i][k].size >= grid[i][j].size:
                break
        
        visibilityRight = 0

        for k in range(j + 1, len(grid[i])):
            visibilityRight += 1
            if grid[i][k].size >= grid[i][j].size:
                break

        visibilityUp = 0

        for k in range(i - 1, -1, -1):
            visibilityUp += 1
            if grid[k][j].size >= grid[i][j].size:
                break

        visibilityDown = 0

        for k in range(i + 1, len(grid)):
            visibilityDown += 1
            if grid[k][j].size >= grid[i][j].size:
                break
                
        max_scene = max(max_scene, visibilityDown * visibilityLeft * visibilityRight * visibilityUp)

print(max_scene)