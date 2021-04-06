
def dakiti(sentence):
    txt_lst = sentence.split(' ')
    txt_sort = sorted(txt_lst, key=lambda x: int("".join([i for i in x if i.isdigit()])))
    return ' '.join([''.join([j for j in i if not j.isdigit()]) for i in txt_sort])

