
def getdivisors(num):
  return [x for x in range(1,num)if num%x==0]
​
def check_perfect(num):
  return sum(getdivisors(num))==num

