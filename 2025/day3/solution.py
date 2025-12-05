with open('input.txt', 'r') as f:
    batteries = [l.strip() for l in f]

def get_joltage_size_two(batteries):
    total_joltage = 0
    for bank in batteries:
        joltage1 = bank[0]
        for j1 in bank[1:-1]:
            if j1 > joltage1:
                joltage1 = j1
        idx = bank.index(joltage1)
        joltage2 = bank[idx+1]
        for j2 in bank[idx+1:]:
            if j2 > joltage2:
                joltage2 = j2

        total_joltage += int(f"{joltage1}{joltage2}")
    return total_joltage



total_joltage = 0
for bank in batteries:
    threshold = len(bank) - 12
    joltage = ""
    last_idx = 0

    for _ in range(11):
        current_idx = last_idx 
        comparison = bank[current_idx]
        best_idx = current_idx

        while current_idx <= threshold:
            j = bank[current_idx]
            if j > comparison:
                comparison = j
                best_idx = current_idx
            current_idx += 1

        last_idx = best_idx + 1
        threshold += 1
        joltage += comparison

    print(joltage)
    total_joltage += int(joltage)

print(total_joltage)
