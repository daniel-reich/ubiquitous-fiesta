
def can_put(txt, dim):
​
    rows = dim[0]
    columns = dim[1]
​
    i = 1
    rem = 10000
​
    words = txt.split()
    for word in words:
        if len(word) > columns:
            return False
        if i <= rows:
            if rem < len(word):
                i += 1
                rem = 10000
            else:
                rem = columns - (len(word)+1)
        if i > rows:
            return False
​
    return True

