
def fizz_buzz(maximum):
  li=[]
  for ele in range(1,maximum+1):
    if ele%3==0 and ele%5==0:
      li.append("FizzBuzz")
    elif ele%5==0:
      li.append("Buzz")
    elif ele%3==0:
      li.append("Fizz")
    else:
      li.append(ele)
  return li

