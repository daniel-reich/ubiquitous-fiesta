
import re
def unravel(txt):
    lst = re.split(r"(\[.+?\])",txt)
    if len(lst) == 1 and lst[0].isalpha():
        return [txt]
    else:
        final = []
        for i in lst:
            result = comp(i)
            if final == []:
                for i in result:
                    final.append(i)
            else:
                newlst = []
                for i in final:
                    for j in result:
                        elem = i + j
                        newlst.append(elem)
                final = newlst
        return list(sorted(final))
​
def comp(i):
    if len([x for x in i if x not in '[]|']) == len(i):
        return [i]
    elif '|' not in i:
        return [i[1:-1]]
    elif '|' in i:
        lst = i[1:-1].split('|')
        return lst

