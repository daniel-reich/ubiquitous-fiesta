
def expanded_form(num):
  num, l = str(num),len(str(num))
  zeros = ['0' * (l - i - 1)  for i in range(l) if num[i] != '0']
  nums = [num[i] for i in range(l) if num[i] != '0']
​
  return ' + '.join(map(''.join, zip(nums, zeros)))

