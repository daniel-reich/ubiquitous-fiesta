
def shift_sentence(x):
    z = x.split()
    y=[item[0] for item in x.split()]
    y.insert(0,(y.pop()))
    return ' '.join([z[i].replace(z[i][0],y[i],1) for i in range(len(z))])

