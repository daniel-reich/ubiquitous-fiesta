
def win_round(a, b):
 ANum1=max(a)
 a.remove(max(a))
 ANum2=max(a)
 print(ANum1,ANum2)
 CompleteNumber1=int(str(ANum1)+str(ANum2))
 print(CompleteNumber1)
 
 BNum1=max(b)
 b.remove(max(b))
 BNum2=max(b)
 print(BNum1,BNum2)
 CompleteNumber2=int(str(BNum1)+str(BNum2))
 print(CompleteNumber2)
 
 
 if CompleteNumber1>CompleteNumber2:
  return True
 else:
  return False

