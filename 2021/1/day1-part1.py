

with open("puzzleinput.txt") as file:
    array = [int(line) for line in file]
file.close()

count = 0
id = 0
while id < len(array)-1:
    next_id = id + 1
    if array[id] < array[next_id]:
        count += 1
    id += 1

print(count)

