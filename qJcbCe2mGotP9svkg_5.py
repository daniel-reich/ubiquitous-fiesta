
def num_to_google(lst):
  s = ""
  for el in lst:
    if isinstance(el,int):
      el = str(el)
    repeat = 1
    if '0' in el:
      repeat = int(el[el.index('0')::])
      el = el[:el.index('0')]
    if el[-1] == '9':
      break
    if '9' in el:
      el = el[el.index('9')+1::]
    nums = [int(x) for x in el]
    for i in range(repeat):
      for num in nums:
        if num == 1:
          s += 'g'
        elif num == 2:
          s += 'o'
        elif num == 3:
          s += 'l'
        elif num == 4:
          s += 'e'
        elif num == 5 and s:
          s = s[:-1] + s[-1].upper()
        elif num == 6:
          s += '.'
        elif num == 7:
          s = s.capitalize()
        else:
          s = s[::-1]
  
  return s

