
def does_rhyme(txt1, txt2):
  str1=""
  str2=""
  for i in txt1:
    if not i in ['?','.','!']:
      str1+=i
  for j in txt2:
    if not j in ['?','.','!']:
      str2+=j
  return str1[-1].lower()==str2[-1].lower()

