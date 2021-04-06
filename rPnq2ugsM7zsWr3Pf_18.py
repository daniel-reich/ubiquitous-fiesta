
def find_all_digits(lst):
  new,fnl,stg = '','',['0','1','2','3','4','5','6','7','8','9']
  for ls in lst:
      for a in range(len(str(ls))):
          if str(ls)[a] in new:
              new+=('-')
          else: new+=str(ls)[a] 
      new+=' '
      if all(x in new for x in stg):
          return ls
  return "Missing digits!"

