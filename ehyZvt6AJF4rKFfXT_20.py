
def uncensor(txt, vowels):
  new_txt=''
  count=0
  for i in txt:
    if i=="*":
      count+=1
      new_txt+=vowels[count-1]
    else:
      new_txt+=i
  return new_txt

