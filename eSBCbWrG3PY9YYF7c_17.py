
elements = ["Metal", "Water", "Wood", "Fire", "Earth"]
animal  = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Sheep", "Monkey", "Rooster", "Dog", "Pig"]
​
def sexagenary(year):
  a = (year-1900) % 60
  return(elements[((a%10)//2%5)] + " " + animal[a % 12])

