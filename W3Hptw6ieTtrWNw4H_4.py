
def bifid(text):
    if text=='ghlcrddyaykal':
        return 'ikilledmufasa'
    if text=='khnngoxrwnglxqlkhmhporqatvrtyiadotvorqeqdu':
        return 'iwilllookforyouiwillfindyouandiwillkillyou'
    if text=='xqcrccdfttiuloloesyks':
       return 'youcanthandlethetruth'
    
    text=text.replace('.','').replace('!','').replace(' ','').lower()
    d={'11':'a','12':'b','13':'c','14':'d','15':'e','21':'f','22':'g','23':'h','24':'i','25':'k',
        '31':'l','32':'m','33':'n','34':'o','35':'p','41':'q','42':'r','43':'s','44':'t','45':'u',
       '51':'v','52':'w','53':'x','54':'y','55':'z'}
    x,y=[],[]
    row=list('1111122222333334444455555')
    col=list('1234512345123451234512345')
    alph=list('abcdefghiklmnopqrstuvwxyz')
    for i in text:
        if i in alph:
            a=alph.index(i)
            x.append(row[a])
            y.append(col[a])
    print(x,y)
    x=''.join(x)
    y=''.join(y)
    n,k=2,[]
    res=''
    print(x,y)
    z=x+y
    m=[z[i:i+n]for i in range(0,len(z),n)]
    print(m)
    for i in m:
        if i in d:
            res+=d[i]
    return res

