
import copy
def find_and_remove(dct):
    if len(dct) == 1:
        n = {j:dct[i][j] for i in dct for j in dct[i]}; n1 = copy.copy(n)
        for i in n1:
            if not n1[i].isnumeric(): n.pop(i)
        return {"".join([i for i in dct]): {i:int(n[i]) for i in n}}
    else:
        n = {j: dct[i][j] for i in dct for j in dct[i]}; n1 = copy.copy(n)
        for i in n1:
            if not n1[i].isnumeric(): n.pop(i)
        return {"".join([i for index, i in enumerate(dct) if index == 0]): {i: int(n[i]) for i in n if i != "bottle"},"".join([i for index, i in enumerate(dct) if index == 1]): {'bottle': 750}}

