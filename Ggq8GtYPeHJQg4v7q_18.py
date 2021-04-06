
def replace_vowels(txt, ch):
    list1 = list(txt)
    for i in range(len(list1)):
        if list1[i] in ["a","e","i","o","u"]:
            list1[i] = ch
    return "".join(list1)

