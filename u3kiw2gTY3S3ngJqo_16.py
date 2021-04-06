
def superheroes(heroes):
  lst = [x for x in heroes if x[-3:] == "man" and x[-4:] != "oman"]
  lst.sort()
  return lst

