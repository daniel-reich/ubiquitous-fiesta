
def is_shuffled_well(lst):
  
  First = 0
  Second = 1
  Third = 2
  Length = len(lst)
  
  while (Third < Length):
    Item_A = lst[First]
    Item_B = lst[Second]
    Item_C = lst[Third]
  
    Test_A = Item_B - Item_A
    Test_B = Item_C - Item_B
    
    if (Test_A == 1) and (Test_B == 1):
      return False
    elif (Test_A == -1) and (Test_B == -1):
      return False
    else:
      First += 1
      Second += 1
      Third += 1
  
  return True

