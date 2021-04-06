
def sum_round(num):
  fin = []
  for i in range(len(str(num))):
    num,res = divmod(num,10)
    if res!=0:
      fin.append(str(res*10**i))
  return ' '.join(fin)

