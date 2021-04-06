
def bugger(num):
  return 0 if num < 10 else 1 + bugger(eval("*".join(str(num))))

