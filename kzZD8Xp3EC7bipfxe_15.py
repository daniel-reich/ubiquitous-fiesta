
def worded_math(equ):
  nums = ['Zero', 'One', 'Two']
  n = {'zero':'0', 'one':'1', 'two':'2', 'plus':'+', 'minus':'-'}
  return nums[eval(''.join(n[i.lower()] for i in equ.split(' ')))]

