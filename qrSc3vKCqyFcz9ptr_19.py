
def sum_round(num):
  return " ".join(x+"0"*i for i,x in enumerate(str(num)[::-1]) if x!="0")

