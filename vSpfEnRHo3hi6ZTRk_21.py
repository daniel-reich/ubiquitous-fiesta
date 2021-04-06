
def free_throws(success, rows):
  
  PreStep_S1 = str(success)
  PreStep_S2 = PreStep_S1.replace("%","")
  PreStep_S3 = int(PreStep_S2)
  PreStep_S4 = float(PreStep_S3 * 0.01)
  PreStep_S5 = round(PreStep_S4, 2)
  Occurrence = PreStep_S5
  
  Decimal = Occurrence ** rows
  Number = Decimal * 100
  Percentage = int(round(Number,0))
  
  Answer = str(Percentage) + "%"
  
  return Answer

