
def straight_digital(number):
  l=list(str(abs(number))[::-1])
  r=[int(l[i])-int(l[i+1]) for i in range(len(l)-1)]
  s=sum(r)/(len(l)-1)
  return "Not Straight" if number <100 or s!=r[0] else "Trivial Straight" if s==0 else r[0]

