
def largest_gap(lst):
    lst2 = []
    s = sorted(lst)
    for i in range(0,len(s)):
        lst2.append(s[i]-s[i-1])
    return max(lst2)

