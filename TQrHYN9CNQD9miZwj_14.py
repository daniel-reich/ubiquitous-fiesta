
def fix_import(s):
    new=s.split()
    [a,b,c,d]=new
    order= ' '.join([c,d,a,b])
    return order

