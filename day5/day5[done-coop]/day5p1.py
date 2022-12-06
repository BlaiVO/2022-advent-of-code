class Pila:

	def __init__(self, array):
		self.array = array

	def move_pack(self, num):
		moved_pck = []
		for _ in range(num):
			moved_pck.append(self.array[-1])
			del self.array[-1]
		return moved_pck

	def move_pack_perf(self, num):
		darrere = num * -1
		moved_pck = []
		while darrere < 0:
			moved_pck.append(self.array[darrere])
			darrere += 1
		for _ in range(num):
			del self.array[-1]
		return moved_pck

def read_header(f, limit = 8):
    stack = []
    for _ in range(9):
        stack.append([])
    for i in range(limit):
        j = 0
        y = 0
        while j < len(f[i]):
            if f[i][j] == '[':
                stack[y].append(f[i][j + 1])
            j += 4
            y += 1
    for i in stack:
        i.reverse()
    return stack


def read_input(data):
	newdata = []
	for element in data:
		newelement = ""
		for lletra in element:
			if lletra in "1234567890 ":
				newelement += lletra
		newdata.append([int(element) for element in newelement.strip() if element != ' '])
	for element in newdata:
		if len(element) != 3:
			element[0] = element[0] * 10 + element[1]
			element.remove(element[1])
	return newdata

if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.readlines()

    data = read_input(data)
    llista_piles = []
    
    with open("header.txt") as f:
        llista_piles.append([Pila(llista) for llista in read_header(f.readlines())])
        llista_piles = llista_piles[0]

    """     for instruction in data:
        llista_piles[instruction[2] - 1].array += llista_piles[instruction[1] - 1].move_pack(instruction[0])

    for pila in llista_piles:
        print(pila.array[-1], end="") """

    # uncomment for part 2
    for instruction in data:
        llista_piles[instruction[2] - 1].array += llista_piles[instruction[1] - 1].move_pack_perf(instruction[0])

    print("P2: ", end="")
    for pila in llista_piles:
        print(pila.array[-1], end="")