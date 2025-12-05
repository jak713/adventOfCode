

with open("puzzleinput.txt") as f:
    array = [l for l in f]
f.close()
# filter the array multiple times to only leave values that have a certain (most common) bit arrangement for oxygen rating and least common for CO2 rating,

def filter_most_common(arr, i):
    if len(arr) == 1:
        print(f"oxygen is: {int(arr[0], 2)}")
        return int(arr[0], 2)
    
    else:   
        count_1 = 0
        count_0 = 0
        ones = []
        zeroes = []
    
        for rate in arr:
            if i>=len(rate):
                print("STOP THIS MADNESS")
                return
            if rate[i] == "1":
                count_1 += 1
                ones.append(rate)
            elif rate[i] == "0":
                count_0 += 1
                zeroes.append(rate)

        if count_1 >= count_0:
            arr = ones 
        else:
            arr = zeroes

        return filter_most_common(arr, i+1)
    

def filter_least_common(arr, i):
    if len(arr) == 1:
        print(f"co2 is: {int(arr[0], 2)}")
        return int(arr[0], 2)

    else:   
        count_1 = 0
        count_0 = 0
        ones = []
        zeroes = []
    
        for rate in arr:
            if i>=len(rate):
                print("STOP THIS MADNESS")
                return
            if rate[i] == "1":
                count_1 += 1
                ones.append(rate)
            elif rate[i] == "0":
                count_0 += 1
                zeroes.append(rate)

        if count_1 >= count_0:
            arr = zeroes 
        else:
            arr = ones

        return filter_least_common(arr, i+1)


o2 = filter_most_common(array, 0)
co2 = filter_least_common(array, 0)
print(f"answer is o2*co2: {o2*co2}")

