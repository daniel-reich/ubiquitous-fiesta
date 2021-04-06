
def parse_code(txt):
  templist = txt.split("0")
​
  while "" in templist:
      templist.remove("")
​
  templist2 = ["first_name", "last_name", "id"]
​
  return dict(zip(templist2, templist))

