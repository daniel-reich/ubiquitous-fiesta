
def is_super_d(n):
  def test(n, d):
​
    tnum = str(d * n**d)
​
    count = 0
    consecuative = False
​
    for n in range(0, len(tnum)):
​
      item = tnum[n]
​
      i = int(item)
​
      if i == d:
        if consecuative == False:
          count += 1
          consecuative = True
        elif consecuative == True:
          count += 1
          if count == d:
            return True
      if i != d:
        if consecuative == True:
          consecuative = False
          count = 0
    
    return False
  
  tests = []
​
  for num in range(2, 10):
​
    t = test(n, num)
​
    if t == True:
      return 'Super-{d} Number'.format(d = num)
    
  return "Normal Number"

