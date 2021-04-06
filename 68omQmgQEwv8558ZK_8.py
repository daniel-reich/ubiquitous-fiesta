
# Check the Resources tab for the list of characters and items.
def max_stats(character,gold):
  if character=="Knight":
      attack,defense,speed=120,140,6
​
  elif character=="Warrior":
      attack,defense,speed=180,71,8
​
  elif character=="Fairy":
      attack,defense,speed=71,100,16
​
  elif character=="Robot":
      attack,defense,speed=160,120,11
​
  elif character=="Giant":
      attack,defense,speed=160,200,4
      
  if 20<=gold<24:
      attack+=10
  elif 24<=gold<30:
      attack+=10
      speed+=3
  elif 30<=gold<40:
      attack+=10
      speed+=3
      defense+=20
  elif 40<=gold<48:
      attack+=20
      speed+=3
      defense+=20
  elif 48<=gold<60:
      attack+=20
      speed+=6
      defense+=20
  elif 60<=gold<72:
      attack+=30
      speed+=6
      defense+=40
  elif 72<=gold<80:
      attack+=30
      speed+=9
      defense+=40
  elif 80<=gold<90:
      attack+=40
      speed+=9
      defense+=40
  elif 90<=gold<96:
      attack+=40
      speed+=9
      defense+=60
  elif 96<=gold<100:
      attack+=40
      speed+=12
      defense+=60        
  elif 100<=gold<120:
      attack+=50
      speed+=12
      defense+=60
  elif 120<=gold<150:
      attack+=50
      speed+=15
      defense+=80
  elif gold>=150:
      attack+=50
      speed+=15
      defense+=100
​
  return [attack,defense,speed]

