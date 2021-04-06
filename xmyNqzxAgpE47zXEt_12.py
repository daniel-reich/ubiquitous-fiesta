
def is_alphabetically_sorted(sentence):
    for e in sentence.split(" "):
        e = e.replace(".", "")
        if len(e) > 2:
            if e ==''.join(sorted(e)):
                return True
            else:
                continue
    return False

