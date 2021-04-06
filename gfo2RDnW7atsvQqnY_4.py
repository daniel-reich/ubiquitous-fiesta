
def count_smileys(lst):
  smiley = 0
  for i in lst:
    if (len(i)==2 and\
      (i[0]==":" or i[0]==";") and\
      (i[1]==")" or i[1]=="D")):
      smiley = smiley+1
    if (len(i)==3 and\
      (i[0]==":" or i[0]==";") and\
      (i[1]=="~" or i[1]=="-") and\
      (i[2]==")" or i[2]=="D")):
      smiley = smiley+1
    
  return smiley

