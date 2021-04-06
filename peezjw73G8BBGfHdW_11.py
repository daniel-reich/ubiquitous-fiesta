
import operator
def arithmetic_operation(n):
    a = int(n.split()[0])
    b = n.split()[1]
    c = int(n.split()[2])
   
    ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '//': operator.floordiv 
}
    try:
        return ops[b](a,c)
    except ZeroDivisionError :
        return -1

