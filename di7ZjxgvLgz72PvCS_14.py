
def validate_swaps(lst, txt):
    holder = []
    while lst:
        to_eval = list(lst.pop(0))
        for char in range(len(to_eval) - 1):
            for i in range(char, len(to_eval)):
                new = to_eval.copy()
                new[char], new[i] = new[i], new[char]
                if "".join(new) == txt: 
                    holder.append(True)
                    break
            else:
                continue  
            break
        else:
            holder.append(False)
    return holder

