
def sexagenary(year):
  elem = {0:"Metal ", 2:"Water ", 4:"Wood ", 6:"Fire ", 8:"Earth "}
  anim = {4:"Rat",5:"Ox",6:"Tiger",7:"Rabbit",8:"Dragon",9:"Snake",10:"Horse",11:"Sheep",0:"Monkey",1:"Rooster",2:"Dog",3:"Pig"}
  
  return elem[(year-year%2)%10] + anim[year%12]

