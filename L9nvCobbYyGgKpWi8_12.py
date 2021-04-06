
def to_list(num):
    res = [int(x) for x in str(num)]
    return res
​
​
​
def to_number(lst):
    s = [str(i) for i in lst]
    res = int("".join(s))
    return res

