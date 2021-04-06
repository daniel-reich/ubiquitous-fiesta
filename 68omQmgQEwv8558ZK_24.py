
# Check the Resources tab for the list of characters and items.
def max_stats(character, gold):
  attack=0
  defense=0
  speed=0
  if character == 'Knight':
    attack=120
    defense=140
    speed=6
  elif character == 'Robot':
    attack=160
    defense=120
    speed=11
  elif character == 'Warrior':
    attack=180
    defense=71
    speed=8
  elif character == 'Fairy':
    attack=71
    defense=100
    speed=16
  elif character == 'Giant':
    attack=160
    defense=200
    speed=4
  
  
  #weapons
  if gold>=100:
    attack+=50
  elif gold>=80:
    attack+=40
  elif gold>=60:
    attack+=30
  elif gold>=40:
    attack+=20
  elif gold>=20:
    attack+=10
  #defense
  if gold>=150:
    defense+=100
  elif gold>=120:
    defense+=80
  elif gold>=90:
    defense+=60
  elif gold>=60:
    defense+=40
  elif gold>=30:
    defense+=20
  #speed
  if gold>=120:
    speed+=15
  elif gold>=96:
    speed+=12
  elif gold>=72:
    speed+=9
  elif gold>=48:
    speed+=6
  elif gold>=24:
    speed+=3
  return [attack,defense,speed]

