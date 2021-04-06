
def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
        print(x,y)
    return x
​
def fractions(decimal):
    rep = decimal.split("(")[1].split(")")[0]
    num1 = decimal.split("(")[0].replace(".", "") + rep
​
    p_index = decimal.index(".")
    exp1 = decimal.index("(") -1-p_index
    exp2 = decimal.index(")")-2 - p_index
​
    num2 = num1[0:exp1+p_index]
    num = int(num1)-int(num2)
​
    bot = 10**exp2-10**exp1
    d = gcd(num, bot)
    return(str(int(num/d)) + "/" + str(int(bot/d)))

