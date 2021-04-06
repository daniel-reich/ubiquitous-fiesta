
def price_importance_sort(dct,b):
    total,newdct,totalprice=[],{},0
    def valof(item,ia):
        return dct[list(dct.keys())[list(dct.keys()).index(item)]][ia]
    for i in list(dct.keys()):
        price,imps=valof(i,'price'),valof(i,'importance')
        newdct.update({price/imps: i})
    newdctnums=sorted(newdct)
    for i in newdctnums:
        if valof(newdct[i],'price')+totalprice<=b:
            total.append(newdct[i])
            totalprice+=valof(newdct[i],'price')
        else:
            return sorted(total)

