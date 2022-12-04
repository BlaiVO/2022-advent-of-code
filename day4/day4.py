file = "pairs.txt"
def get_ab(pair):
	raw_ab = pair.split(",")
	a = raw_ab[0].split("-")
	b = raw_ab[1].split("-")
	for i in range(2):
		a[i], b[i] = int(a[i]), int(b[i])
	return a, b

def p1(file):
	pairs = open(file).readlines()
	fully_contained = 0
	for pair in pairs:
		a, b = get_ab(pair)
		if (a[0] <= b[0] and a[1] >= b[1]) or (b[0] <= a[0] and b[1] >= a[1]):
			fully_contained += 1
	return fully_contained

def p2(file):
	pairs = open(file).readlines()
	overlapped = 0
	for pair in pairs:
		a, b = get_ab(pair)
		if not(a[1] < b[0] or a[0] > b[1]):
			overlapped += 1
	return overlapped

print(f"p1: {p1(file)}")
print(f"p2: {p2(file)}")