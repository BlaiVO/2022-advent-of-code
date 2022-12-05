file = "boxes.txt"

def read_header(f, limit = 8):
    stack = []
    for _ in range(9):
        stack.append([])
    for i in range(limit):
        j, y =  0, 0
        while j < len(f[i]):
            if f[i][j] == '[':
                stack[y].append(f[i][j + 1])
            j += 4
            y += 1
    for i in stack:
        i.reverse()
    return stack

def p1(file):
    f = file.open(file).readlines()
    stack = read_header(f)
    for line in f:
        if line.startswith("next"):
            line = line.split(" ")
            moves = line[1]
            src = line[3]
            dst = line[5]
            


f = open(file).readlines()
for i in read_header(f):
    print(i)

