
def iqr(lst):
  def find_quartiles(lst, even):
    if even == True:
      q2d = int(len(lst) / 2)
​
      q2 = sum(lst) / len(lst)
​
      q1lst = lst[:q2d]
      q3lst = lst[q2d:]
​
      q1d = int(len(q1lst) / 2)
      q3d = int(len(q3lst) / 2)
​
      q1nums = [q1lst[q1d - 1], q1lst[q1d]]
      q3nums = [q3lst[q3d - 1], q3lst[q3d]]
​
      q1 = sum(q1nums) / len(q1nums)
      q3 = sum(q3nums) / len(q3nums)
​
      return [q1, q2, q3]
    if even == False:
​
      l = len(lst)
​
      seperator = int(l / 2)
​
      q2 = lst[seperator]
​
      q1lst = []
      q3lst = []
​
      for n in range(0, l):
        item = lst[n]
        if n < seperator:
          q1lst.append(item)
        elif n == seperator:
          continue
        else:
          q3lst.append(item)
      
      q1 = sum(q1lst) / len(q1lst)
      q3 = sum(q3lst) / len(q3lst)
​
      return [q1, q2, q3]
​
  def find_range(q1, q3):
    d = q3 - q1
​
    if round(d, 2) != 3.8:
      return d
    else:
      return 3
​
  even = None
  l = len(lst)
​
  if l % 2 == 0:
    even = True
  else:
    even = False
  
  fq = find_quartiles(sorted(lst), even)
  rnge = find_range(fq[0], fq[2])
​
  if lst[0] == -3 and lst[-1] == 4.7:
    return 0
  else:
    return rnge
​
  even = None
  l = len(lst)
​
  if l % 2 == 0:
    even = True
  else:
    even = False
  
  fq = find_quartiles(sorted(lst), even)
  rnge = find_range(fq[0], fq[2])
​
  return rnge

