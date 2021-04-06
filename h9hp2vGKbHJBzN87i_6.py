
def partially_hide(phrase):
​
    phrase_lst = phrase.split()
​
    mod_lst = []
​
    for item in phrase_lst:
​
        if len(item) > 2:
​
            new_item = item[0] + ("-" * (len(item) -2)) + item[-1]
​
            mod_lst.append(new_item)
​
        else:
​
            mod_lst.append(item)
​
    return " ".join(mod_lst)

