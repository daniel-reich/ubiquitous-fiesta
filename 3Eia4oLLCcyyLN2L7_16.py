
def remove_repeats(s):
    arr = []
    for i in range(len(s))[:-1]:
        if s[i] != s[i + 1]:
            arr.append(s[i])
​
    return "".join(arr)+(s[-1])

