
def freq_count(list1, key):
    x = -1
    dict1 = {}
    list2 = []
​
    def freq_count_2(lst, ky):
        nonlocal x
        nonlocal dict1
        x += 1
        total = 0
        for item in lst:
            if type(item) == list:
                freq_count_2(item, ky)
            elif item == ky:
                total += 1
        try:
            dict1[x] += total
        except:
            dict1[x] = total
        x -= 1
    freq_count_2(list1, key)
    for i in sorted(dict1.keys()):
        list2.append([i, dict1[i]])
    return list2

