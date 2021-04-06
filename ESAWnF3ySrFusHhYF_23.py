
def edit_words(lst):
  new_lst=[]
  for word in lst:
    if len(word)>0:
      if len(word)%2==0:
        hyp_pos = len(word)/2
      else:
        hyp_pos = int(len(word)/2)+1
      count = 0
      new_word = ""
    else:
      new_word = "-"
    for letter in list(reversed(word)):
      letter = letter.upper()
      if count+1 == hyp_pos:
        hyphenation = letter+"-"
        new_word+=hyphenation
        count+=1
      else:
        new_word+=letter
        count+=1
    new_lst.append(new_word)
    
  return new_lst

