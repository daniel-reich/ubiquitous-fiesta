
def anagram(name, words):
  name=name.lower()
  fname=name[0:name.find(' ')]
  lname=name[name.find(' ')+1:len(name)]
  name=fname+lname
  total=len(name)
  dict={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'x':0,'x':0,'y':0,'z':0}
  for letter in name:
    count=name.count(letter)
    dict[letter]=count
    
  for i in range(len(words)):
    for char in words[i]:
      if dict[char]==0:
        return False
      else:
        dict[char]-=1
        total-=1
  if total!=0:
    return False
  else:
    return True

