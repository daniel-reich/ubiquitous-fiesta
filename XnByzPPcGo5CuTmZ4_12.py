
import string
​
def kix_code(addr):
    lst = addr.split(",")
    lst[2] = lst[2].replace(" ","")
    output = ""
    for index, i in enumerate(lst[2]):
        if index < 6:
            output += i
    for index, i in enumerate(lst[1]):
        try:
            int(i)
            x = index
            break
​
        except:
            pass
            
    for i in lst[1][index:]:
        if i in "0123456789" or i in string.ascii_letters:
            try:
                int(i)
                output += i
                continue
            except:
                output += i.upper()
        else:
            output += "X"
​
    return output

