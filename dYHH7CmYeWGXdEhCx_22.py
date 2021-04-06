
def word_builder(let, pos):
    A=[(y,x) for (x,y) in zip(let, pos)]
    B=sorted(A)
    C=''
    for k in B:
      C=C+k[1]
    return C

