
def turn_calc(num):
  a = str(num)
  str1 = a.replace('.','')
  b = str1.replace('1','I').replace('2','Z').replace('3','E').replace('4','H').replace('5','S').replace('6','G').replace('7','L').replace('8','B').replace('0','O')
  return b[::-1]

