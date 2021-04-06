
def build_staircase(quantity, character):
  stairs = []
  stair = []
  count = 0
  while len(stairs) < quantity:
      stair = []
      for i in range(quantity):
          if i <= count:
              stair.append(character)
          else:
              stair.append("_")
      stairs.append(stair)
      count += 1
​
  return stairs

