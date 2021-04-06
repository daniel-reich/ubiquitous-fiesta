
def anagram(name,lst):
​
    namelist = []
    for i in name:
        namelist += i.lower()
    for i in lst:
        for x in i:
            if x in namelist:
                namelist.remove(x)
            else: return False
    return namelist == [' ']

