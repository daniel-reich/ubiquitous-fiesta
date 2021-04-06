
import re
​
def does_rhyme(txt1, txt2):
  txt1, txt2 = txt1.lower().split()[-1], txt2.lower().split()[-1]
  print(re.findall('[aeiou]', txt1)[-2:], re.findall('[aeiou]', txt2)[-2:])
  return re.findall('[aeiou]', txt1.lower())[-2:] == re.findall('[aeiou]', txt2.lower())[-2:]

