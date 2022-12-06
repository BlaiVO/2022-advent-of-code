file = "data.txt"

def get_x_different(line, x):
	for i in range(len(line)):
		current = []
		for y in range(x):
			current.append(line[i + y])
		if len(current) == len(set(current)):
			return i + x

def p1(file):
	data = open(file).readlines()[0]
	return get_x_different(data, 4)

def p2(file):
	data = open(file).readlines()[0]
	return get_x_different(data, 14)

print(f"p1: {p1(file)}")
print(f"p2: {p2(file)}")