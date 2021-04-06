
def increasing_word_weights(s):
    x = lambda i: [ord(l) for l in i if l.isalpha()]
    y = [sum(x(w)) for w in s.split()]
    return y == sorted(y)

