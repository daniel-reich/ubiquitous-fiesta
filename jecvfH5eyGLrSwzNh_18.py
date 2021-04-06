
def fauna_number(txt):
    ani = ["muggercrocodile", "one-hornedrhino", "python", "moth", "monitorlizard", "bengaltiger"]
    lst = txt.replace(',', ' ').split()
    return sorted([(i, lst[ele-1]) for i in ani for ele, j in enumerate(lst) if i == j], key = lambda x: x[0])

