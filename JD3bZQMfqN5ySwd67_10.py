
def is_vampire(n):
​
    import itertools
    num_1 = str(n)
    l = list(itertools.permutations(num_1))
    string = ''
    l_1, l_2 = [], []
    for x in l:
        for y in x:
            string = string + y
        l_1.append(string)
        string = ''
​
    if n < 100:
        return "Normal Number"
    elif len(num_1) % 2 == 0:
        for item in l_1:
            l_2.append(int(item[:len(item) // 2]) * int(item[len(item) // 2:]))
    else:
        for item in l_1:
            l_2.append(int(item[:(len(item) // 2 + 1)]) * int(item[(len(item) // 2) + 1:]))
            l_2.append(int(item[:len(item) // 2]) * int(item[len(item) // 2:]))
​
    if n in l_2 and len(num_1) % 2 == 0:
        return "True Vampire"
    elif n in l_2:
        return "Pseudovampire"
    else:
        return "Normal Number"

