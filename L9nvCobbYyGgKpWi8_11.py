
def to_list(num):
  return [int(digit) for digit in str(num)]
​
def to_number(lst):
  return int(''.join([str(number) for number in lst]))

