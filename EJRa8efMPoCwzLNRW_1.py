
def dakiti(sentence):
    x= ','.join(sorted(sentence.split(),key=lambda x:int(''.join([i for i in x if i.isdigit()]) ) ) ).split(',')
    f= ' '.join(x)
    return ''.join( i for i in f if not i.isdigit())

