
from string import punctuation
def pig_latin(txt):
    punc_mark = txt[len(txt) - 1]
    txt = ''.join([x for x in list(txt) if x not in punctuation])
    txt = txt.replace('.', '')
    txt_split = txt.split(' ')
    new_txt = []
    for index, w in enumerate(txt_split):
        if w[0].lower() in ['a', 'e', 'i', 'o', 'u']:
            new_txt.append(w + 'way')
            continue
        if w[0].lower() not in ['a', 'e', 'i', 'o', 'u'] and len(w) == 1:
            new_txt.append(w + 'ay')
            continue
        w_lst = list(w)
        w_lst = [x.lower() for x in w_lst]
        first_letter = w_lst[0]
        w_lst.append(first_letter)
        w_lst = w_lst[1:] + ['ay']
        if index == 0:
            w_lst[0] = w_lst[0].upper()
        w_lst = ''.join(w_lst)    
        new_txt.append(w_lst)
    return ' '.join(new_txt) + punc_mark

