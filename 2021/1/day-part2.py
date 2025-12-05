with open("puzzleinput.txt") as file:
    array = [int(line) for line in file]

sum_three = []
idx = 0
while idx < len(array)-2:
    sum_three.append(array[idx]+array[idx+1]+array[idx+2])
    idx += 1

idx = 0
count = 0
while idx < len(sum_three)-1:
    if sum_three[idx]<sum_three[idx+1]:
        count += 1
    idx += 1


print(count)
