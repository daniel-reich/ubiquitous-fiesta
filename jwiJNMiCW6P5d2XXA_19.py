
import re
def does_rhyme(txt1, txt2):
  txt1,txt2 = txt1.split()[-1],txt2.split()[-1]
  return sorted([i.lower() for i in re.findall(r'[aeiou]',txt1,flags=re.IGNORECASE)])==sorted([i.lower() for i in re.findall(r'[aeiou]',txt2,flags=re.IGNORECASE)])

