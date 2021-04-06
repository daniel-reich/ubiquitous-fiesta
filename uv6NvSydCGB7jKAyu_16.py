
def is_parsel_tongue(sentence):
    for word in sentence.lower().split():
        if "s" in word and "ss" not in word:
            return False
    return True

