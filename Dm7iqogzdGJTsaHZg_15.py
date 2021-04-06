
def retrieve(txt):
    vowels = 'aeiou'
    result_lst = []
    txt.lower()
    lst = txt.lower().split(' ')
    if len(txt) == 0:
        return([])
    for i in lst:
        if i[0] in vowels and i[-1] != '.':
            result_lst.append(i)
        elif i[0] in vowels and i[-1] == '.':
            result_lst.append(i[:-1])
    return(result_lst)

