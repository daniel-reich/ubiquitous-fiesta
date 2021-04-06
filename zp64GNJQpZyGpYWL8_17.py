
def score_it(s):
  def nest(string, index):
​
    nsts = 0
​
    for n in range(index + 1):
      item = string[n]
      if item == '(':
        nsts += 1
      if item == ')':
        nsts -= 1
    
    return nsts
  def integers(lst, string):
    together = []
    near = []
​
    for idx in lst:
      if near == []:
        near.append(idx)
      else:
        if idx == max(near) + 1:
          near.append(idx)
        else:
          together.append(near)
          near = [idx]
    
    if near != []:
      together.append(near)
    del near
    
    numbers = []
    
    for lst in together:
      nums = []
      for idx in lst:
        try:
          nums.append(str(int(string[idx])))
        except ValueError:
          pass
      if len(nums) != 0:
​
        num = ''.join(nums)
        numbers.append(int(num))
    
    if len(numbers) == 0:
      return [0]
    return numbers
​
  nests = {}
​
  for n in range(len(s)):
    nst = nest(s, n)
    if nst not in nests.keys():
      nests[nst] = [n]
    else:
      nests[nst].append(n)
  
  nest_vals = {}
​
  for ky in nests.keys():
    nest_vals[ky] = integers(nests[ky], s)
  
  score = 0
​
  for val in nest_vals.keys():
    integers = nest_vals[val]
​
    for integer in integers:
      score += (integer * val)
    
  return score

