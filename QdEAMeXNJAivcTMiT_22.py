
def boxes(weights):
  sum = 0;
  boxes = 1;
  for x in weights:
    sum += x;
    if(sum>10):
      sum = x;
      boxes = boxes+1;
  return boxes;

