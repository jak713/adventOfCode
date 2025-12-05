
with open("puzzleinput.txt") as f:
    array = [l for l in f]

n = len(array[0]) - 1

counts = {}
for i in range(n):
    counts[str(i)] = [0,0]

for num in array:
    for i in range(n):
        if num[i] == "1":
            i = str(i)
            counts[i][1] += 1
        elif num[i] == "0":
            i = str(i)
            counts[i][0] += 1

gamma = "0b"
epsilon = "0b"
for value in counts.values():
    if value[0] > value[1]:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"
print(counts, gamma, epsilon)
print(f"gamma: {int(gamma, 2)} and epsilon: {int(epsilon, 2)}, power consumption =  {int(epsilon, 2)*int(gamma, 2)},")
