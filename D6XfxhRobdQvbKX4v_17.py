
def first_before_second(s, first, second):
  string = [char for char in s]
  ioffirst = []
  iofsecond = []
  for i in range(0, len(string)):
    if first == string[i]:
      ioffirst.append(i)
    if second == string[i]:
      iofsecond.append(i)
  if ioffirst[-1] < iofsecond[0]:
    return True
  else: 
    return False

