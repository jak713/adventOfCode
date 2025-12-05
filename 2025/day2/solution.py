"""
Product ID ranges is what we are given, they come as number ranges like 1-10 separated by commas. Problem is, all the ones that are a sequence of digits repeated twice (55, 6464, 123123, etc) are invalid. Hence, we have to set all the invalid IDs aside and sum them up. 
"""

with open('input.txt', 'r') as f:
    inputs = f.readline().strip().split(',')
    f.close()

# This is possibly a brute force approach:
# For each entry in the list, split it by '-' and then iterate over numbers in range [0]-[1]+1 of the entry
# If length of number is odd, ignore
# Split each number in 2 if it's length is even (meaning there can be a sequence repeated twice) and compare the two halves - if they are the same, the ID is invalid.

def find_invalid_ids(ranges: list) -> list:
    invalid_ids = []
    for r in ranges:
        r = r.split('-')
        lower = int(r[0])
        higher = int(r[1])
        for i in range(lower, higher+1):
            i = str(i)
            if len(i)%2 != 0:
                continue
            else:
                mid = int(len(i)/2)
                part1 = i[0:mid]
                part2 = i[mid:]
                if part1 == part2:
                    invalid_ids.append(int(i))
    return invalid_ids

print(f"The answer to the first part is: {sum(find_invalid_ids(inputs))}")

def unpack_ranges(ranges: list) -> list:
    ids = []
    for r in ranges:
        r = r.split('-')
        lower = int(r[0])
        higher = int(r[1])
        for i in range(lower, higher+1):
            ids.append(str(i))
    return ids

# In this case, rather than sequences repeated twice, it is sequences repeated at least twice. The length can be used to create the possible sequences instead. 
def get_invalid_ids(ids:list) -> list:
    invalid_ids = []
    for i in ids:
        length = len((i))
        if length == 1:
            continue
        possiblities = [i[0]*length]
        if length == 4:
            possiblities.append(i[:2]*2)
        if length == 6:
            possiblities.append(i[:2]*3)
            possiblities.append(i[:3]*2)
        if length == 8:
            possiblities.append(i[:2]*4)
            possiblities.append(i[:4]*2)
        if length == 9:
            possiblities.append(i[:3]*3)
        if length == 10:
            possiblities.append(i[:2]*5)
            possiblities.append(i[:5]*2)
        
        if i in possiblities:
            invalid_ids.append(int(i))
    return invalid_ids


print(sum(get_invalid_ids((unpack_ranges(inputs)))))  