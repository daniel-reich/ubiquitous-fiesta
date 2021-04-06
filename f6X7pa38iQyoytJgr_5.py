
def increasing_word_weights(sentence):
    import string
    a=string.punctuation
    x=[]
    for i in sentence.split():
        y=[]
        for j in i:
            if j not in a:
                y.append(ord(j))
        x.append(sum(y))
    return True if x==sorted(x) else False

