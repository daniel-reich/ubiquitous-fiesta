
def trouble(num1,num2):
    x=['111','222','333','444','555','666','777','888','999','000']
    a=str(num1)
    b=str(num2)
    y=[i for i in x if i in a]
    if y==[]:
        return False
    z=b.count(y[0][:2])
    if z>=1:
        return True
    else:
        return False

