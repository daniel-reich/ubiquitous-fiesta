
def is_astonishing(num):
  partitions  = [ [int(left) , int(right)] for (left , right) in get_partition(str(num))];
  for partition in partitions:
    a,b = partition;
    partition_sum = get_sequence_sum(a,b);
    if (partition_sum == num):
      return "{}-Astonishing".format("AB" if a < b else "BA");
  return False;
  
def get_partition(seq):
  return [ [seq[:idx] , seq[idx:]] for idx in range(1 ,len(seq))];
  
def get_sequence_sum(a , b):
  begin , end =  (a,b) if a < b else (b,a)
  one_to_end_sum  = (end*(end+1))/2;
  one_to_begin_sum = (begin*(begin-1))/2;
  return one_to_end_sum - one_to_begin_sum;

