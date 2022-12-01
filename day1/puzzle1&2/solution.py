import numpy as np

f = open("puzzleInput.csv", "r")

data = f.read().split("\n")

calorie_sums = []

total = 0
for i in data:
    if i != "":
        total += int(i)
    else:
        calorie_sums.append(total)
        total = 0

print(max(calorie_sums))

sorted_calorie_sums = sorted(calorie_sums)
print(sum(sorted_calorie_sums[-3:]))
