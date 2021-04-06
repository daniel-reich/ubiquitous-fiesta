
def num_then_char(lst):
  def seperator(lst):
    list_lengths = {}
    numbers = []
    l8rs = []
    for n in range(len(lst)):
      length = len(lst[n])
      list_lengths[n] = length
      for item in lst[n]:
        if isinstance(item, int) == True or isinstance(item, float) == True:
          numbers.append(item)
        else:
          l8rs.append(item)
    return list_lengths, numbers, l8rs
  def combiner(lengths, inputs):
    
    lsts = []
​
    for n in range(len(list(lengths.keys()))):
      
      lst = []
      count = 0
      goal = lengths[n]
​
      while count < goal:
        lst.append(inputs[0])
        inputs.pop(0)
        count += 1
      
      lsts.append(lst)
    
    return lsts
​
​
  s = seperator(lst)
​
  lengths = s[0]
  numbers = sorted(s[1])
  l8rs = sorted(s[2])
​
  inputts = numbers + l8rs
​
  c = combiner(lengths, inputts)
​
  return c

