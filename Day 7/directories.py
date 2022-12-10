class Directory:
    name : str
    files : list['Files']
    subdirectories : list['Directory']
    parentDir : 'Directory' = None
    size : int = -1

    def __init__(self, name, parentDir = None) -> None:
        self.name = name
        self.parentDir = parentDir
        self.files = []
        self.subdirectories = []

    def sizeComp(self) -> int:
        if self.size != -1:
            return self.size
        sum = 0
        for file in self.files:
            sum += file.size
        for dir in self.subdirectories:
            sum += dir.sizeComp()

        self.size = sum
        return self.size


class Files:
    name : str
    size : int

    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size

f = open("input.txt", "r")
dirs = []
currDir = None

for line in f.readlines():
    args = line.strip().split()
    if args[0] == "$":
        if args[1] == "cd":
            if args[2] == "/":
                root_dir = Directory("root")
                currDir = root_dir
                dirs.append(root_dir)
            elif args[2] == "..":
                currDir.sizeComp()
                currDir = currDir.parentDir
            else:
                for dir in currDir.subdirectories:
                    if dir.name == args[2]:
                        currDir = dir
                        break
    else:
        if args[0] == "dir":
            dir = Directory(args[1], currDir)
            currDir.subdirectories.append(dir)
            dirs.append(dir)
        else:
            currDir.files.append(Files(args[1], int(args[0])))

dir_sizes = [x.sizeComp() for x in dirs]
print(sum(x for x in dir_sizes if x <= 100000))

size_on_system = dir_sizes[0]

dirs.sort(key = lambda x: x.sizeComp())

free_size = 70000000 - size_on_system

for dir in dirs:
    if free_size + dir.sizeComp() >= 30000000:
        print(dir.sizeComp())
        break
