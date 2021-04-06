
from itertools import repeat
def grant_the_hint(txt):
    txt = txt.split(" ")
    txt_len = len(txt)
    holder,final = [], []
    longest = len(max(txt, key = len))
    counter = 0
    while txt:
        elem = txt.pop(0)
        holder.append(elem)
        holder.extend(repeat(elem, longest - len(elem)))
        for char in elem[::-1]:
            k = elem.rfind(char)
            elem = elem[:k] + ("_" * (len(elem) - len(elem[:k])))
            holder.append(elem)
    step = int(len(holder) / txt_len)
    while counter < step:
        final.append(" ".join([holder[x] for x in range(counter, len(holder), step)]))
        counter += 1
    return final[::-1]

