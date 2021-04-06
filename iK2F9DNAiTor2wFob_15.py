
def calc(s):
  num1 = list("".join(str(ord(x)) for x in s))
  num2 = list("".join(num1).replace("7","1"))
  return sum(int(x) for x in num1)-sum(int(x) for x in num2)

