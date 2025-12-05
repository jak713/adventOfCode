
with open("puzzleinput.txt") as file:
    array = [line for line in file]

route = {
        "depth":0,
        "horizontal":0
        }

for direction in array:
    direction = direction.split()
    value = int(direction[1])
    if "forward" in direction[0]:
        route["horizontal"] += value
    elif "down" in direction[0]:
        route["depth"] += value
    else:
        route["depth"] -= value
print(route)
answer = route["depth"] * route["horizontal"]
print(answer)
