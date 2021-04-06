
def first_n_vowels(txt, n):
    vowels = ["a", "e", "i", "o", "u"]
    ret = []
    j = 0
    s = ""
​
    for i in txt:
        # print(i)
        if j < n:
            #   print("inside 2")
            if i in vowels:
                #   print("inside")
                ret.append(i)
                j += 1
    if len(ret) < n:
        return "invalid"
    else:
        return s.join(ret)

