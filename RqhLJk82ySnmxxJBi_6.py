
def power_morphic(num):
  sayac=0
  for i in range(2,10):
    sayi=str(pow(num,i))
    son=int(sayi[-len(str(num)):])
    if(son==num):
      sayac+=1
  if sayac==8:
    return "Polymorphic"
  elif sayac==4:
    return "Quadrimorphic"
  elif sayac==2:
    return "Dimorphic"
  elif sayac==1:
    return "Enamorphic"
  elif sayac==0:
    return "Amorphic"

