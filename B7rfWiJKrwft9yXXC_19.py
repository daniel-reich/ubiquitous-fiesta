
def sort_decending(num) :
    a=sorted(str(num),reverse=True)
    b=""
    for i in a :
       b+=i
    return int(b)

