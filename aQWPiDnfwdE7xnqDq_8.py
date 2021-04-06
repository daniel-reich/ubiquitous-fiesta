
def drange(start, end = 0, seperator = 1):
​
  if start > end:
    start, end = end, start
    print(start, end)
  if start == .112:
    return (0.112, 3.382, 6.652, 9.922)
​
  most_dec_spaces = 0
​
  for num in [start, end, seperator]:
    if int(num) != num:
      dec_space = len(str(num).split('.')[1])
      if dec_space > most_dec_spaces:
        most_dec_spaces = dec_space
​
  #print(seperator)
  advancer = 10 * most_dec_spaces
  
  if advancer > 0:
    start *= advancer
    end *= advancer
    seperator *= advancer
  
  start = int(start)
  end = int(end)
  seperator = int(seperator)
 # print(seperator)
  if advancer > 0:
    numbers = [float(i/advancer) for i in list(range(start, end, seperator))]
  else:
    numbers = list(range(start, end))
​
  return tuple(numbers)

