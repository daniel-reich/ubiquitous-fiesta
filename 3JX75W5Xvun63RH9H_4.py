
def describe_num(n):
  d = {
  1: 'brilliant'  , 2: 'exciting'   , 3: 'fantastic'  ,
  4: 'virtuous' , 5: 'heart-warming', 6: 'tear-jerking' ,
  7: 'beautiful'  , 8: 'exhilarating' , 9: 'emotional'  ,
  10: 'inspiring' }
  
  quals = [d[x] for x in d if not n % x]
  
  return 'The most {} number is {}!'.format(' '.join(quals), n)

