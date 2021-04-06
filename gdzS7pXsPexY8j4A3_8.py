
def count_digits(lst, t):
  
  new = []
  count_arr = []
  count = 0
​
  for i in range(len(lst)):
      new.append(str(lst[i]))
​
  for i in range(len(new)):
      for y in range(len(new[i])):
          num = int(new[i][y])
          x = num % 2 != 0 if t == 'odd' else num % 2 == 0
          if x:
              count += 1
      count_arr.append(count)
      count = 0
​
  return count_arr

