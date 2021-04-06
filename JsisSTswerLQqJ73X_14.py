
def priority_sort(lst, s):
    lst.sort()
    
    if not lst or not s:
        return lst
​
    s, l = list(s)[::-1], []
​
    while s:
        num = s.pop()
        counter = lst.count(num)
​
        for i in range(counter):
            lst.remove(num)
            l.append(num)
​
    return l + lst

