
def count_lone_ones(n):
  count = 0
  n_str = str(n)
  for i in range(0, len(str(n))):
    if len(n_str) > 1:
      if int(n_str[i]) == 1:
        if i == 0 and int(n_str[i+1]) != 1:
          count += 1
        elif i + 1 == len(n_str) and int(n_str[i-1]) != 1:
          count += 1
        elif int(n_str[i-1]) != 1 and int(n_str[i+1]) != 1:
          count += 1
    else:
      count += n_str.count('1')
  return count

