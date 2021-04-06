
def get_middle(word):
    arr = word[:len(word) // 2]
    arr2 = word[len(word) // 2:]
​
    if len(word) <= 1:
        return word
    elif len(word) % 2 != 0:
        return arr2[0]
    return str(arr[-1] + arr2[0])

