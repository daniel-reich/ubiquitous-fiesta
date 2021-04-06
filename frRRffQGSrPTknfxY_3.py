
def digit_count(n):
  num_counts = dict()
  str_n = str(n)
  
  for x in str_n:
    if x not in num_counts: num_counts[x] = 1
    else: num_counts[x] += 1
  
  return int( "".join( str(num_counts[x]) for x in str_n ) )

