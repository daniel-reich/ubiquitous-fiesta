
def perimeter(lst):
  
  # Working Out Length of Side 1
  
  Side_01_H = abs(lst[0][0] - lst[1][0])
  Side_01_V = abs(lst[0][1] - lst[1][1])
  
  A_Squared = Side_01_H ** 2
  B_Squared = Side_01_V ** 2
  C_Squared = A_Squared + B_Squared
  
  TSL1_Length = C_Squared ** 0.5
  
  # Working Out Length of Side 2
  
  Side_02_H = abs(lst[1][0] - lst[2][0])
  Side_02_V = abs(lst[1][1] - lst[2][1])
  
  A_Squared = Side_02_H ** 2
  B_Squared = Side_02_V ** 2
  C_Squared = A_Squared + B_Squared
  
  TSL2_Length = C_Squared ** 0.5
  
  # Working Out Length of Side 3
  
  Side_03_H = abs(lst[2][0] - lst[0][0])
  Side_03_V = abs(lst[2][1] - lst[0][1])
  
  A_Squared = Side_03_H ** 2
  B_Squared = Side_03_V ** 2
  C_Squared = A_Squared + B_Squared
  
  TSL3_Length = C_Squared ** 0.5
  
  # Working Out Perimeter of Triangle
  Perimeter = TSL1_Length + TSL2_Length + TSL3_Length
  
  # Rounding and Giving Answer
  Answer = round(Perimeter,2)
  return Answer

