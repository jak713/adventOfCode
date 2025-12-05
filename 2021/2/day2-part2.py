

with open("puzzleinput.txt") as f:
    array = [l for l in f]

route = {
	"depth":0,
	"horizontal":0,
	"aim":0
}

for direction in array:
    direction = direction.split()
    value = int(direction[1])

    if "forward" in direction[0]:
        route["horizontal"] += value
        route["depth"] += route["aim"] * value
    elif "down" in direction[0]:
        route["aim"] += value
    else:
        route["aim"] -= value

print(route)
print(route["depth"]*route["horizontal"])

