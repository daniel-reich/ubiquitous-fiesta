
import re
def same_length(txt):
  lst = []
  if txt.count('0') == txt.count('1'):
    for n in range(1, int(txt.count('1')/2)):
      chk = re.compile(r'(1{'+str(n)+ '})(?=0{' +str(n)+ '})')
      if re.search(chk, txt):
        lst.append(True)
      else:
        lst.append(False)
    return all(lst)
  else:
    return False

