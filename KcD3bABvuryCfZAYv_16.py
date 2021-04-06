
def most_frequent_char(lst):
    k=''.join(lst)
    import collections
    c=collections.Counter(k)
​
    maximum = max(c.values())
    keys = [key for key, value in c.items() if value == maximum]
​
    keys.sort()
    return(keys)

