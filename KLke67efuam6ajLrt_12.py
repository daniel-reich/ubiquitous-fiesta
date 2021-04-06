
def generate(num):
  oAry = []
  for i in range(num):
    oAry.append(i)
  return oAry
  
def outShuffle(ary):
  n = int(0.5*len(ary) )
  first = ary[:-n]
  second = ary[n:]
  oAry = []
  for i in range(n):
    oAry.append(first[i])
    oAry.append(second[i])
  return oAry
​
def shuffle_count(num):
  ref = generate(num)
  test = generate(num)
  count = 0
  for i in range(num):
    count = count + 1
    test = outShuffle(test)
    if test == ref: 
      break
  return count

