
def choose_fuse(fuses, current):
  
  CV_PreStep1 = str(current)
  CV_PreStep2 = CV_PreStep1.replace("V","")
  CV_PreStep3 = float(CV_PreStep2)
  Current_Value = CV_PreStep3
  
  Counter = 0
  Length = len(fuses)
  
  Best = 99
  
  while (Counter < Length):
    
    Item = fuses[Counter]
    
    F_PreStep1 = str(Item)
    F_PreStep2 = F_PreStep1.replace("V","")
    F_PreStep3 = float(F_PreStep2)
    Fuse_Value = F_PreStep3
    
    if (Fuse_Value < Best) and (Fuse_Value >= Current_Value):
      Best = Fuse_Value
      Counter += 1
    else:
      Counter += 1
  
  Answer = str(Best) + "V"
  Answer = Answer.replace(".0","")
  
  return Answer

