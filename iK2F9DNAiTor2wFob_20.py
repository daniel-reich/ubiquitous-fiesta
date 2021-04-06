
def calc(s: str):
    ascii_s = [str(ord(x)) for x in s]
    num1 = "".join(ascii_s)
    num2 = num1.replace("7", "1")
    sum1 = sum([int(x) for x in num1])
    sum2 = sum([int(x) for x in num2])
    return sum1 - sum2

