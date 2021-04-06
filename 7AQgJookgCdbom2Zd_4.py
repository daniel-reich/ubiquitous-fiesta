
def pig_latin(txt):
  txtList = txt.split()
  tempPunc = txtList[-1][-1]
  txtList[-1] = txtList[-1][:-1]
  #Removes the period from the last word in the list of words
  newString = ""
  temp = ""
  
  #Converts each word to pig latin
  for i in range (len(txtList)):
    if txtList[i][0] in ('a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'):
      txtList[i]+="way"
    else:
      txtList[i].lower()
      temp = txtList[i][0]
      txtList[i] = txtList[i][1:]
      txtList[i]+= temp + "ay"
    
  #Capitalizes the first letter of the first word
  txtList[0] = txtList[0].capitalize()    
  
  #Adds all pig latin words into new string
  for i in range (len(txtList)):
    newString+=txtList[i] + " "
    
  newString = newString[:-1]
  newString+=tempPunc
  
  return newString

