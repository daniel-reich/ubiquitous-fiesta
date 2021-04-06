
def time_to_eat(ct):
    h, p = int(ct[:ct.find(':')]), ct[ct.find('.')-1]=='p'
    m = int(ct[ct.find(':')+1:ct.find(' ')])
    h = 7-h-int(m>0) if p else 12-h-int(m>0) if 7<=h<12 else 7-h-int(m>0)
    m = 60 - m if m > 0 else m
    return [h if h>=0 else 12+h ,m]

