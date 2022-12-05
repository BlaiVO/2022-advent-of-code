rock = {
    "other": "A",
    "self": "X",
    "score": 1
}
paper = {
    "other": "B",
    "self": "Y",
    "score": 2
}
scissors = {
    "other": "C",
    "self": "Z",
    "score": 3
}
results = {
    "loose": 0,
    "draw": 3,
    "win": 6
}

filename = "rps.txt"

def get_round_score(o, s):
    round_score = 0
    if s == rock["self"]:
        round_score += rock["score"]

        if o == scissors["other"]:
            round_score += results["win"]
        elif o == rock["other"]:
            round_score += results["draw"]

    elif s == paper["self"]:
        round_score += paper["score"]

        if o == rock["other"]:
            round_score += results["win"]
        elif o == paper["other"]:
            round_score += results["draw"]

    else:
        round_score += scissors["score"]
        
        if o == paper["other"]:
            round_score += results["win"]
        elif o == scissors["other"]:
            round_score += results["draw"]
    return round_score

def p1(file):
    score = 0
    with open(file) as f:
        matches = f.readlines()
        for match in matches:
            score += get_round_score(match[0], match[2])
    return score

def p2(file):
    ...
print(f"p1: {p1(filename)}")
