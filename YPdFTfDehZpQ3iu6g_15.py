
def roman_numerals(arg):
  rom2num = dict(zip('IVXLCDM',[1,5,10,50,100,500,1000]))
  num2rom = [(v,k) for k,v in rom2num.items()] + [(4,'IV'),(9,'IX'),(40,'XL'),(90,'XC'),(400,'CD'),(900,'CM')]
  if type(arg) == str:
    res = 0
    for i,c in enumerate(arg):
      if i < len(arg)-1 and rom2num[c] < rom2num[arg[i+1]]:
        res -= rom2num[c]
      else:
        res += rom2num[c]
  else:
    res = ''
    for num,rom in sorted(num2rom)[::-1]:
      i,arg = divmod(arg,num)
      res += rom*i
  return res

