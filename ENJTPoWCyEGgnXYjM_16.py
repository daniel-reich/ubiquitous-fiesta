
def percent_filled(box):
  os = 0;
  blanks = 0;
  for row in box:
    os += len([i for i in row if i == 'o'])
    blanks += len([i for i in row if i == ' '])
  
  return str(round(os/(blanks+os)*100)) + '%'

