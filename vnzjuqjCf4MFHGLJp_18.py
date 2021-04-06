
def shift_letters(txt, n):
    whitespaces = [pos for pos in range(len(txt)) if txt[pos] == " "]
    lst = [char for char in txt if char != " "]
    holder = []
    for i in range(len(lst)):
        i += n
        if i >= len(lst):
            i = i % len(lst)
        holder.append(i)
    final = list("".join([x[1] for x in sorted(list(zip(holder, lst)))]))
    for j in whitespaces:
        final.insert(j, " ")
    return("".join(final))

