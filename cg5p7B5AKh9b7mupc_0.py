
def check_inclusion(s1, s2):
    len_s1, len_s2 = len(s1), len(s2)
    arr1 = [0] * 26
    for c in s1:
        idx = ord(c) - 97
        arr1[idx] += 1
    arr2 = [0] * 26
    for c in s2[:len_s1]:
        idx = ord(c) - 97
        arr2[idx] += 1
    if arr1 == arr2:
        return True
    for i in range(len_s2 - len_s1):
        left = ord(s2[i]) - 97
        arr2[left] -= 1
        right = ord(s2[i + len_s1]) - 97
        arr2[right] += 1
        if arr1 == arr2:
            return True
    return False

