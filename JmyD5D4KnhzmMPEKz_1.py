
def constraint(txt):
    if pangram(txt):
        return "Pangram"
    elif heterogram(txt):
        return "Heterogram"
    elif tautogram(txt):
        return "Tautogram"
    elif transgram(txt):
        return "Transgram"
    else:
        return "Sentence"
​
​
def get_chars(txt):
    lst = []
    for char in txt:
        if char.isalpha():
            lst.append(char.lower())
    return lst
​
​
def pangram(txt):
    correct = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
               'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    lst = get_chars(txt)
​
    if sorted(set(lst)) == correct:
        return True
    return False
​
​
def heterogram(txt):
    lst = get_chars(txt)
​
    for char in lst:
        if lst.count(char) != 1:
            return False
    return True
​
​
def tautogram(txt):
    lst = txt.split(" ")
    first = lst[0][0].lower()
​
    for word in lst:
        if word[0].lower() != first:
            return False
    return True
​
​
def transgram(txt):
    lst = sorted(txt.split(" "), key=len)
    check = []
​
    for char in lst[0]:
        is_successful = True
​
        for i in range(len(lst)):
            if char.lower() not in lst[i].lower():
                check.append(0)
                is_successful = False
                break
        
        if is_successful:
            check.append(1)
    
    if 1 in check:
        return True
    return False

