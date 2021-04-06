
def count_lone_ones(n):
  num = str(n)
  count = 0
  for i in range(len(num)):
    if num[i] == "1":
      if len(num) == 1:
        count += 1
      elif i == 0 and len(num) > 1:
        if num[i+1] != "1":
          count += 1
      elif i == len(num) - 1:
        if num[i-1] != "1":
          count += 1
      elif num[i-1] != "1" and num[i+1] != "1":
        count += 1
  return count

