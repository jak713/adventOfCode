with open('input.txt', 'r') as f:
    ranges = []
    inputs = []
    in_ranges = True
    for line in f:
        if line == '\n':
            in_ranges = False
            continue
        if in_ranges:
            ranges.append(line.strip())
        else:
            inputs.append(line.strip())

def get_range(rng: str) -> list:
    """
    Unfortunately too heavy for github codespaces. Will need to rethink obtaining ranges. Perhaps substring matching?
    
    :param rng: e.g. '1-5'
    :type rng: str
    :return: e.g. would give [1,2,3,4,5]
    :rtype: list
    """
    rng_list = rng.split('-')
    return rng_list


# binary search? surely not because the ranges overlap and we would have to do very many of lookups... ok better idea could be to just check
# which of the inputs are both <= higher bound and >= lower bound

fresh = 0
for inp in inputs:
    found = False
    for r in ranges:
        rng = get_range(r)
        if not found:
            if int(rng[0]) <= int(inp) <= int(rng[1]):
                fresh += 1
                found = True
        else:
            continue
print(fresh)
print(len(inputs))