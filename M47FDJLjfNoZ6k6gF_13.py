
def cup_swapping(swaps):
  positions = ['A','B','C']
  position_number = 1
  for eachswap in swaps:
    #position 1
    if 'A' in eachswap and 'B' in eachswap and position_number == 1:
      position_number = 0
    elif 'C' in eachswap and 'B' in eachswap and position_number == 1:
      position_number = 2
    #position 2
    elif 'B' in eachswap and 'C' in eachswap and position_number == 2:
      position_number = 1
    elif 'A' in eachswap and 'C' in eachswap and position_number == 2:
      position_number = 0
    #position 0
    elif 'B' in eachswap and 'A' in eachswap and position_number == 0:
      position_number = 1
    elif 'C' in eachswap and 'A' in eachswap and position_number == 0:
      position_number = 2
  return positions[position_number]

