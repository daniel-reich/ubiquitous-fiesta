
def encryption(txt):
    txt = txt.replace(" ", "")
    x = len(txt)
    rows = round(x**0.5)
    for i in range(rows+3):
        if i*rows >= x:
            columns = i
            break
    table = [txt[i:i+columns] for i in range(0, x, columns)]
    output = ""
    for i in range(columns):
        for j in table:
            try:
                output += j[i]
            except:
                break
        if i != columns-1:
            output += " "
    return output
            
        
            
​
print(encryption("haveaniceday"))
print(encryption("feedthedog"))
print(encryption("chillout"))
print(encryption("A Fool and His Money Are Soon Parted."))

