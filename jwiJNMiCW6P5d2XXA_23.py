
def does_rhyme(txt1, txt2):
  txt1=txt1.lower()
  txt2=txt2.lower()
  lst=[]
  lst2=[]
  vowels=[]
  vowels2=[]
  txt1=txt1.replace('.','')
  txt1=txt1.replace('!','')
  txt1=txt1.split(' ')
  for i in txt1:
    lst.append(i)
  one=lst[-1]
  txt2=txt2.replace('.','')
  txt2=txt2.replace('!','')
  txt2=txt2.split(' ')
  for i in txt2:
    lst2.append(i)
  two=lst2[-1]
  for i in one:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
      vowels.append(i)
  for i in two:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
      vowels2.append(i)
  if(vowels==vowels2):
    return True
  else:
    return False

