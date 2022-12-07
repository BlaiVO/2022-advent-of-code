file = "commands.txt"

def p1(file):
	console = open(file).readlines()
	filesystem = {}
	current_dir = ""
	last_dir = []
	for output in console:
		output = output.split(" ")
		if output[0] == "$" and output[1] == "cd":
			if output[2] == "..":
				current_dir = last_dir[-1]
				last_dir.remove(current_dir)
			else:
				last_dir.append(output[2])
				current_dir
