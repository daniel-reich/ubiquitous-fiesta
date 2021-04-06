
def min_removals(txt1, txt2):
    # not using sets because of cases such as:
    # print(min_removals("kkk", "kk") == 1)
    # print(min_removals("kkxx", "kkx") == 1)...
​
    shortest = txt2 if len(txt2) <= len(txt1) else txt1
    longest = txt1 if shortest == txt2 else txt2
    shared = [1 for ch in shortest if ch in longest]
​
    return (len(txt1) - len(shared)) + (len(txt2) - len(shared))

