
def coconut_translator(txt):
  lst = ['0' + bin(ord(i))[2:] if i.isalpha() else '00' + bin(ord(i))[2:] for i in txt]
  result = []
  nuts = 'coconuts'
  for i in range(len(lst)):
    res = ''
    for j in range(len(lst[i])):
      if lst[i][j] == '0':
        res += nuts[j].lower()
      else:
        res += nuts[j].upper()
    result.append(res)
    res = ''
  return ' '.join(result)

