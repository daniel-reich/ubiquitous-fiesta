
def is_parsel_tongue(sentence):
    sentence = sentence.lower().split()
    ss = [word for word in sentence if "s" in word]
    for word in ss:
        if word.count("ss") >= 1:
            continue
        else:
            return False
    return True

