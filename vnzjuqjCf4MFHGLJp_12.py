
def shift_letters(txt, n):
    new, c = "", 0
    sent =  "".join(txt.split())
    sent = sent[-n%len(sent):] + sent[:-n%(len(sent))]
    for i in txt:
        if i == " ": new += " "
        else: new += sent[c]; c += 1
    return new

