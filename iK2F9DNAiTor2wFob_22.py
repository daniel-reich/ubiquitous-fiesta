
def calc(s):
    num1="".join([str(ord(x)) for x in s])
    a=sum([int(x) for x in num1])
    num2=num1.replace("7", "1")
    b=sum([int(x) for x in num2])
    return a-b

