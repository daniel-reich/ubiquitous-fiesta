
import re
def most_common_words(text, n):
    lst, d = re.findall(r"\b\w+\b", text.lower()), dict()
    for w in lst:
        if w in d:
            d[w] += 1
        else:
            d[w] = 1
    lst_d = sorted([(k, v) for k, v in d.items()],
                   key=lambda tpl: (-tpl[1], lst.index(tpl[0])))
    return {t[0]: t[1] for t in lst_d[:min(n, len(lst_d))]}

