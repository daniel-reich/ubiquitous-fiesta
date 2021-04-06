
def is_rectangle(coordinates):
  from ast import literal_eval
  #-----cell is just used for making rectangles-----#
  if len(coordinates) != 4:
    return False
  rectangle = coordinates
    
  #-----converts from str to tuples-----#
  rectangle = [literal_eval(i) for i in rectangle]
  rectangle = [list(i) for i in rectangle]
  
  #-----making the coords into usable variables-----#
  (ax, ay), (bx, by), (cx, cy), (dx, dy) = rectangle
  xAxis= [ax, bx, cx, dx]
  yAxis= [ay, by, cy, dy]
  xAxis.sort()
  yAxis.sort()
  
  #-----setting up variables to be referenced at end-----#
  xPairs = False
  yPairs = False
  
  #-----checking if there are two pairs of x and y values in rectangle-----#
  if xAxis[0] == xAxis[1]:
    xAxis.reverse()
    if xAxis[0] == xAxis[1]:
      xPairs = True
  if yAxis[0] == yAxis[1]:
    yAxis.reverse()
    if yAxis[0] == yAxis[1]:
      yPairs = True
    
  #-----checking if True-----#
  if xPairs and yPairs == True:
    return True
  else:
    return False

