import numpy as np

f = open("puzzleInput.csv", "r")

data = f.read().split("\n")


def rps_score(round):
    round_score = 0
    if round[1] == "X":
        round_score += 0
        if round[0] == "A":
            round_score += 3
        elif round[0] == "B":
            round_score += 1
        elif round[0] == "C":
            round_score += 2
    elif round[1] == "Y":
        round_score += 3
        if round[0] == "A":
            round_score += 1
        elif round[0] == "B":
            round_score += 2
        elif round[0] == "C":
            round_score += 3
    elif round[1] == "Z":
        round_score += 6
        if round[0] == "B":
            round_score += 3
        elif round[0] == "C":
            round_score += 1
        elif round[0] == "A":
            round_score += 2
    print(round_score)
    return round_score


rounds = []

for round in data:
    rounds.append(round.split(" "))

print(rounds)

score = 0
for round in rounds:
    score += rps_score(round)

print(score)
