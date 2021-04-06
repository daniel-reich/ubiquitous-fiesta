
def parse_roman_numeral(num):
    t=old=0
    order='IVXLCDM'
    val=[1,5,10,50,100,500,1000]
    for i in num[::-1]:
        new=order.index(i)
        if new>=old:
            t+=val[new]
        else:
            t-=val[new]
        old=new
    return t

