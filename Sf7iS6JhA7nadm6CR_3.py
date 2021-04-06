
def remainder(num):
  seq = [1, 10, 9, 12, 3, 4]
  return sum([int(i) * seq[idx % 6] for idx, i in enumerate(str(num)[::-1])])
​
def divisibility_rule(num):
  rem = remainder(num)
  return num if rem == num else divisibility_rule(rem)

