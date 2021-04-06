
def sweetest_icecream(lst):
  flavours = {"Plain": 0,
        "Vanilla": 5,
        "ChocolateChip": 5,
        "Strawberry": 10,
        "Chocolate": 10
        } 
  
  return max([flavours[ice_cream.flavor] + ice_cream.num_sprinkles for ice_cream in lst])

