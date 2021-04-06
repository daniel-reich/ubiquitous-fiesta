
def cup_swapping(swaps):
    arr = [i for i in range(len(swaps)) if "B" in swaps[i]]
    if not arr: return "B"
    letter = ""
    for i in swaps[arr[0]]:
        if i != "B":
            letter = i
​
    for i in range(len(swaps))[arr[0] + 1:]:
        if letter in swaps[i]:
            for x in swaps[i]:
                if x != letter:
                    letter = x
                    break
    return letter

