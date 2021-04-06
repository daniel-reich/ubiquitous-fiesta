
def fruit_salad(fruits):
    res =[]
    for word in fruits:
        res.append(word[:len(word)//2])
        res.append(word[len(word)//2:])
    return  ''.join(sorted(res))

