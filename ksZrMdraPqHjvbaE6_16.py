
def largest_even(lst):
    m = {k: k % 2 for k in lst}
    lar = {k: k // 2 for k in lst}
    print(m)
    print(lar)
    biggest = [0, 0]
    for i in m:
        if m[i] == 0:
            if lar[i] > biggest[1]:
                biggest = [i, lar[i]]
​
    return biggest[0] if biggest[0] else -1

