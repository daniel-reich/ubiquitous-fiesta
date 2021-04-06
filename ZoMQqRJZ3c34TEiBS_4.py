
def playfair(txt,keyword):
    offset = 0 if ' ' in txt else -2
    remaining_letters = set('abcdefghiklmnopqrstuvwxyz') - set(keyword)
    table = ''.join(sorted(set(keyword),key=keyword.index)).upper()+\
            ''.join(sorted(remaining_letters)).upper()
    text = txt.upper().replace(' ','').replace('J','I')\
                      .replace('.','').replace(':','')
    
    def chars_from_table(chars):
        y1,x1 = divmod(table.index(chars[0]),5)
        y2,x2 = divmod(table.index(chars[1]),5)
        if y1==y2:
            x1,x2=(x1+1+offset)%5,(x2+1+offset)%5
        elif x1==x2:
            y1,y2=(y1+1+offset)%5,(y2+1+offset)%5
        else:
            x1,x2 = x2,x1
        return table[(5*y1+x1)%25]+table[(5*y2+x2)%25]
    
    result = ''
    while len(text)>1:
        if text[0] != text[1]:
            result += chars_from_table(text[:2])
            text = text[2:]
        else:
            result += chars_from_table(text[0]+'X')
            text = text[1:]
    if text:
        result += chars_from_table(text[0]+'X')
    return result

