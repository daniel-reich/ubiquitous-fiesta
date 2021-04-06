
def fix_import(s):
  txt = [i for i in s.split()]
  
  return txt[2] +' ' +  txt[3] +' ' +  txt[0] + ' ' + txt[1]

