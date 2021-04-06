
def letters(word1, word2):
    arr = []
    for i in word1:
        for x in word2:
            if i == x and i not in arr:
                arr.append(i)
    arr = "".join(sorted(arr))
    arr2 = []
    for i in word1:
        if i not in word2 and i not in arr2:
            arr2.append(i)
    arr2 = "".join(sorted(arr2))
    arr3 = []
    for i in word2:
        if i not in word1 and i not in arr3:
            arr3.append(i)
    arr3 = "".join(sorted(arr3))
​
    return [arr, arr2, arr3]

