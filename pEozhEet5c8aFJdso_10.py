
def all_about_strings(txt):
    result = [len(txt), txt[0], txt[-1], txt[(len(txt)-1)//2:(len(txt)+2)//2]]
    i = txt.find(txt[1])
    j = txt.find(txt[1], i+1)
    if j == -1:
        result.append('not found')
    if j != 0:
        result.append('@ index ' + str(j))
    if result[-1] == '@ index -1':
        result.pop(-1)
    return result

