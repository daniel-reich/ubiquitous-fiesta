
def min_miss_pos(lst):
  newlist = sorted(lst)
  count = 1
  templist = []
​
  for number in newlist:
      if number < 0:
          continue
      else:
          if count not in newlist:
              templist.append(count)
          count += 1
​
  if templist:
      return templist[0]
  else:
      return count

