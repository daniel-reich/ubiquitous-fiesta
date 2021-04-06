
def reverse_sort(txt):
    return " ".join(sorted(txt.split(" "), key=lambda x: (len(x), x.lower()), reverse = True))

