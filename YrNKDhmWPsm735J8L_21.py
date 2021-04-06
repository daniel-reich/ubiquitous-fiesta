
#One line? This is close enough.
def sort_word(word):
    result1 = []
    result2 = []
    result3 = ''
    for i in word:
        if i.isupper():
            result1 += i
        elif i.islower():
            result2 += i
        else:
            result3 += i
    result1.sort()
    result2.sort()
    result1.extend(result2)
    for i in result1:
        result3 += i
    return result3

