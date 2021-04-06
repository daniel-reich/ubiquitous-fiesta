
def reverse_words(words):
    string = ""
    lst = words.split()
    i = len(lst) - 1
    while i >= 0:
        string += lst[i]
        if i != 0:
            string += " "
        i -= 1
    return string

