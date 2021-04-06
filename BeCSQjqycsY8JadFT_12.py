
def recur_index(txt, k=1):
    if txt and len(txt) > 1:
        if txt[k] in txt[:k]:
            return {txt[k]: [txt[:k].index(txt[k]), k]}
        elif k < len(txt) - 2:
            return recur_index(txt, k + 1)
    return dict()

