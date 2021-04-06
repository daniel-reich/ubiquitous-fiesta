
def remix(txt, lst):
  letter = ""
  for i in range(len(txt)):
    letter += txt[lst.index(i)]
    print(letter)
  return letter
  
# append letter where letter index == lst
# find i in lst, use index of that for letter

