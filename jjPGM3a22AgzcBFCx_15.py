
def decrypt(lst):
    for num in range(len(lst)):
        lst[num] += 63
        # return lst
    lst.sort()
    # print(lst)
    for char in range(len(lst)):
        if lst[char] + 1 != lst[char + 1]:
            return chr(lst[char + 1])

