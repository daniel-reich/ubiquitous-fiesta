
def back_to_home(directions):
  dicty={"N":1,"S":-1,"W":1,"E":-1}
  return sum(list(dicty[x] for x in directions))==0;

