
def word_builder(lst,indexes):
    final_lst = [0 for a in range(len(lst))]
    zp = list(zip(lst,indexes))
    for a,b in zp:
        final_lst[b] = a
    return ''.join(final_lst)

