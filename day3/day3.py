from string import ascii_letters as alphabet

f = "rucksacks.txt"

#Part 1
def get_priority(compartment1, compartment2):
	for i in range(len(alphabet)):
		if alphabet[i] in compartment1 and alphabet[i] in compartment2:
			return(i)

def p1(file):
	sacks = open(file).readlines()
	total_priority = 0
	for sack in sacks:
		compartment1, compartment2 = sack[:len(sack)//2], sack[len(sack)//2:]
		total_priority += get_priority(compartment1, compartment2)
	return (total_priority)

#Part 2
def get_common_priority(sack1, sack2, sack3):
	for i in range(len(alphabet)):
		if alphabet[i] in sack1 and alphabet[i] in sack2 and alphabet[i] in sack3:
			return i + 1

def p2(file):
	sacks = open(file).readlines()
	sack1, sack2 = None, None
	total_priority = 0
	for i in range(len(sacks)):
		if (i + 1) % 3 == 0:
			total_priority += get_common_priority(sacks[i], sack1, sack2)	
			sack1, sack2 = None, None
		else:
			if sack1 is None:
				sack1 = sacks[i]
			sack2 = sacks[i]
	return total_priority

print(f"p1: {p1(f)}")
print(f"p2: {p2(f)}")