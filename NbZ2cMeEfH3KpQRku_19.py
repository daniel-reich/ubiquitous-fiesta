
def portion_happy(numbers):
  
  Unhappy_Zeroes = 0
  All_Zeroes = numbers.count(0)
  
  Unhappy_Ones = 0
  All_Ones = numbers.count(0)
​
  First = 0
  Second = 1
  Third = 2
  Length = len(numbers)
  
  while (Third < Length):
    
    Item_A = numbers[First]
    Item_B = numbers[Second]
    Item_C = numbers[Third]
    
    if (Item_A == 0) and (Item_B == 1) and (Item_C == 0):
      Unhappy_Ones += 1
      First += 1
      Second += 1
      Third += 1
    
    elif (Item_A == 1) and (Item_B == 0) and (Item_C == 1):
      Unhappy_Zeroes += 1
      First += 1
      Second += 1
      Third += 1
    
    else:
      First += 1
      Second += 1
      Third += 1
​
​
  if (numbers[0] == 0) and (numbers[1] == 1):
    Unhappy_Zeroes += 1
  
  elif (numbers[0] == 1) and (numbers[1] == 0):
    Unhappy_Ones += 1
  
  else:
    Unhappy_Zeroes += 0
    Unhappy_Ones += 0
  
  
  if (numbers[-2] == 1) and (numbers[-1] == 0):
    Unhappy_Zeroes += 1
  
  elif (numbers[-2] == 0) and (numbers[-1] == 1):
    Unhappy_Ones += 1
    
  else:
    Unhappy_Zeroes += 0
    Unhappy_Ones += 0
​
  Unhappy_Population = Unhappy_Zeroes + Unhappy_Ones
  Population = len(numbers)
  
  Happy_Numbers = 1 - (Unhappy_Population / Population)
  return Happy_Numbers

