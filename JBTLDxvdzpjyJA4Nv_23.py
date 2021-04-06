
import re
def super_reduced_string(txt):
    aux = txt + ' '
    while aux != txt:
        aux = txt
        txt = re.sub(r'((\w)\2)','',txt)
        if not txt:
            return 'Empty String'
    return txt

