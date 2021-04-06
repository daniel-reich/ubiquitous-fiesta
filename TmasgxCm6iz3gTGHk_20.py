
def min_length(lst, num):
  current_minimum_lst = [];
  current_minimum = 69;
  for k in range(0 , len(lst)):
    for m in range(k+1, len(lst)+1):
      if (sum(lst[k:m]) > num and m- k  < current_minimum  ):
          current_minimum_lst =  lst[k:m];
          current_minimum  = m - k;
  return len(current_minimum_lst) or  -1 ;

