
import string
​
def tweak_letters(txt, lst):
    lowers = string.ascii_lowercase
    shift = zip(txt, lst)
    ans = []
    for item in shift:
        ind = (lowers.index(item[0])+item[1])%26
        ans.append(lowers[ind])
    return ''.join(ans)

