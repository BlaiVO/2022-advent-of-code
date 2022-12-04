f = "rps.txt"
results = {
	"A" : {
		"X" : {
			"result_value" : 0,
			"choice_value" : 3
		},
		"Y" : {
			"result_value" : 3,
			"choice_value" : 1
		},
		"Z" : {
			"result_value" : 6,
			"choice_value" : 2
		}
	},
	"B" : {
		"X" : {
			"result_value" : 0,
			"choice_value" : 1
		},
		"Y" : {
			"result_value" : 3,
			"choice_value" : 2
		},
		"Z" : {
			"result_value" : 6,
			"choice_value" : 3
		}
	},
	"C" : {
		"X" : {
			"result_value" : 0,
			"choice_value" : 2
		},
		"Y" : {
			"result_value" : 3,
			"choice_value" : 3
		},
		"Z" : {
			"result_value" : 6,
			"choice_value" : 1
		}
	}
}


def p2(file):
	linesmatches = open(file).readlines()
	total_score = 0
	for match in linesmatches:
		adversary, result = match[0], match[2]
		total_score += results[adversary][result]["result_value"] + results[adversary][result]["choice_value"]
	return total_score

print(f"p2: {p2(f)}")