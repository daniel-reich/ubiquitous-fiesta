
def dial(txt):
  
  List_A = [  "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", 
              "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
              "U", "V", "W", "X", "Y", "Z"  ]
  
  List_B = [  "2", "2", "2", "3", "3", "3", "4", "4", "4", "5", 
              "5", "5", "6", "6", "6", "7", "7", "7", "7", "8",
              "8", "8", "9", "9", "9", "9"  ]
  
  Revised = ""
  Counter = 0
  Length = len(txt)
  
  while (Counter < Length):
    
    Item = txt[Counter]
    Capital = Item.upper()
    
    if (Capital in List_A):
      Place = List_A.index(Capital)
      New = List_B[Place]
      Revised = Revised + New
      Counter += 1
    else:
      Revised = Revised + Item
      Counter += 1
  
  return Revised

