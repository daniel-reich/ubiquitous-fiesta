
def fill_perimeter(lst,txt,width,offset):
    if width == 1:
        lst.extend([(offset,offset,txt[0])])
        return lst
    result = []
    for indx,t in enumerate(txt[0:4*width  - 4]):
        if indx%4 == 0 :
            lst.extend([(0 + offset,indx//4 + offset,t)])
        if indx%4 == 1 :
            lst.extend([((indx-1)//4  + offset, width - 1 + offset ,t)])
        if indx%4 == 2 :
            lst.extend([(width - 1 + offset ,width - 1 - (indx-2)//4  + offset, t)])
        if indx%4 == 3 :
            lst.extend([(width - 1 - (indx-3)//4 +      offset ,0 + offset   , t)])
    if width > 2:
        lst=fill_perimeter(lst,txt[4*width  - 4::],width - 2,offset + 1) 
    return lst
​
def clockwise_cipher(message):
    y = len(message)**(.5)
    if y.is_integer():
        width = int(y)
    else: 
       width = int(y + 1)  
       message = message + (int(y + 1)**2 - len(message))*" "
    lst = fill_perimeter([],message,width  ,0)
    return ''.join([t for x,y,t in sorted(lst)])

