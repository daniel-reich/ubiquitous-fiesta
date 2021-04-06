
import textwrap
def split_n_cases(txt, cases):
    if len(txt)%cases!=0:
        return ['Error']
​
    return textwrap.wrap(txt,len(txt)//cases)

