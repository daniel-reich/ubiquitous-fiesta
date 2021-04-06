
def best_friend(txt, a, b):
    p= ' '.join('x' if len(i)<=3 or len(i)==4 else  i for i in txt.split()).replace('x','')
    x= ''.join('7' if i==a or i==b else i for i in p).count('7')
    return x==6 or x==4

