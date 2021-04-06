
def possibly_perfect(key, answers):
  def decision(k, a):
    correctanswer = k[0]
    studentanswer = a[0]
​
    n = 0
    while correctanswer == '_':
      correctanswer = k[n + 1]
      studentanswer = a[n + 1]
​
      n += 1
​
    if correctanswer == studentanswer:
      return 'S'
    else:
      return 'D'
  def same(k, a):
    
    s = True
​
    for number in range(0, len(k)):
      
      key = k[number]
      ans = a[number]
​
      if key != '_':
        if key != ans:
          s = False
          break
    
    return s
  def different(k, a):
    
    diff = True
​
    for number in range(0, len(k)):
​
      key = k[number]
      ans = a[number]
​
      if key != '_':
        if ans == key:
          diff = False
          break
    
    return diff
​
  d = decision(key, answers)
​
  if d == 'S':
    r = same(key, answers)
  elif d == 'D':
    r = different(key, answers)
  else:
    r = False
​
  return r

