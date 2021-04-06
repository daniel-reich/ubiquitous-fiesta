
def uncensor(txt, vowels):
  txt=list(txt)
  vowels= list(vowels)
​
  for i in range(len(txt)):
      if txt[i]=="*":
          txt[i]=vowels[0]
          vowels.remove(vowels[0])
​
  letter=txt[0]
  for i in range(1,len(txt)):
      letter+=txt[i]
​
  return "{}".format(letter)

