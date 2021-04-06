
def almost_palindrome(txt):
    arr = txt[:len(txt) // 2]
    arr2 = txt[len(txt) // 2:]
    if len(arr2) > len(arr):
        arr2 = arr2[1:]
    if arr2[0] == arr[-1]:
        arr2 = arr2[::-1]
    minimum = [set(arr), set(arr2)]
    minimum.sort(key=len)
    if len(set(arr)) == len(set(arr2)) == 1:
        return False
    return len(set(arr + arr2)) == len(minimum[0]) + 1

