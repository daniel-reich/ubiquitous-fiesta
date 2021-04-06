
def fizz_buzz(maximum):
  out=[]
  for n in range(1,maximum+1):
    if n%15==0: out.append("FizzBuzz")
    if n%3==0 and n%15!=0:  out.append("Fizz")
    if n%5==0 and n%15!=0:  out.append("Buzz")
    if n%3!=0 and n%5!=0: out.append(n)
  return out

