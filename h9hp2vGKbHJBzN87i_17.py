
def partially_hide(phrase):
  phrase = phrase.split()
  counter=0
  while counter <= (len(phrase))-1:
    if len(phrase[counter]) <= 2:
      counter=counter+1
    else:
      nes=phrase[counter]
      counter1=nes[0]
      print(counter1)
      counter2=nes[-1]
      print(counter2)
      counter3= "-"*(len(nes)-2)
      print(counter3)
      counter1=counter1+counter3+counter2
      print(counter1)
      phrase[counter] = phrase[counter].replace(nes,counter1)
      counter=counter+1
  return ' '.join(phrase)

