
def min_removals(s1,s2):
​
    s1_check=[s for s in s1 if s not in s2]
    s2_check = [s for s in s2 if s not in s1]
​
    return len(s1_check)+len(s2_check)

