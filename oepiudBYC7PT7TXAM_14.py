
def parse_roman_numeral(num):
  romandict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
  def lettercalc(focus_letter,comp_letter):
    if romandict.get(focus_letter)<romandict.get(comp_letter):
      return romandict.get(focus_letter)*-1
    else:
      return romandict.get(focus_letter)
  i=0
  value=0
  while i<len(num)-1:
    value+=lettercalc(num[i],num[i+1])
    i+=1
  value+=romandict.get(num[-1])
  return value

