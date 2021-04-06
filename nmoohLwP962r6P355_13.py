
def straight_digital(number):
  if number<0 or number<100:
    return "Not Straight"
  mem=list(set([int(str(number)[i])-int(str(number)[i-1]) for i in range(1,len(str(number)))]))
  return "Trivial Straight" if mem[0]==0\
  else "Not Straight" if len(mem)!=1 else mem[0]

