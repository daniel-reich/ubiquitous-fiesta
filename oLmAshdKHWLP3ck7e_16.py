
def min_difference_pair(nums):
  max_abs_diff = abs(nums[0] - nums[1]);
  tuple_with_minimal_difference = [nums[0] , nums[1]];
  for k in range(0 , len(nums)-1):
    for m in range(k+1 , len(nums)):
      current , other = ( nums[k] , nums[m])
      difference =  abs(current - other);
      
      if (difference < max_abs_diff):
        max_abs_diff = difference;
        tuple_with_minimal_difference = (current , other);
        
      elif (difference  == max_abs_diff ):
        tuple_with_minimal_difference =  (current , other) if sum((current , other)) < sum( tuple_with_minimal_difference) else tuple_with_minimal_difference;
    
  return sorted(tuple_with_minimal_difference);

