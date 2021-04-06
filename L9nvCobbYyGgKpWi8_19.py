
def to_list(num):
  temp = str(num)
  return [int(number) for number in temp]
​
def to_number(lst):
  temp = [str(number) for number in lst]
  return int("".join(temp))

