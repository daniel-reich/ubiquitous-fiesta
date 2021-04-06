
def odds_vs_evens(num):
  s = list(str(num))
  odd_l = []
  even_l =[]
  for i in s:
      if int(i)%2 != 0:
          odd_l.append(i)
​
  for i in s:
      if int(i)%2 == 0:
          even_l.append(i)
  count_1 = 0
  for i in odd_l:
      count_1 += int(i)
  count_2 = 0
  for i in even_l:
    count_2 += int(i)
  if count_1 > count_2:
    return 'odd'
  elif count_1 < count_2:
    return 'even'
  else:
    return 'equal'

