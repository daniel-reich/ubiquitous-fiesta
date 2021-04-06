
def calc(s):
  num1 = "".join(str(ord(c)) for c in s)
  num2 = num1.replace("7","1")
  return sum(int(c) for c in num1) - sum(int(c) for c in num2)

