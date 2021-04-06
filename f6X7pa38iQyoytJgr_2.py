
from string import ascii_letters as abc
​
def increasing_word_weights(t):
​
    l = ''.join([ n for n in t if n in abc+' ' ]).split()
    l =  list(map(lambda x: sum( ord(i) for i in x) ,l))
    l = sum( 1 for i in range(len(l)-1) if l[i+1]-l[i]<=0 )
    return not l

