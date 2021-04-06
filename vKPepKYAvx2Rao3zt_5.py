
def car_timer(n):
  remainder = n%60
  result = n//60
  show = 0
  while True:
    show = show + result%10
    result = result//10
    if result//10==0:
      show = show + result % 10
      break
  while True:
    show = show+remainder%10
    remainder = remainder//10
    if remainder//10==0:
      show = show + remainder % 10
      break
  return show

