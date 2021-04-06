
def even_odd_string(txt):
  odds = ''
  evens = ''
  for i in range(len(txt)):
    if i%2 == 0:
      evens += txt[i]
    else:
      odds += txt[i]
  return evens + ' ' + odds

