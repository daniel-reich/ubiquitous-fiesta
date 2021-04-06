
def shared_digits(lst):
  return all([share_digit(num , other) for num , other in zip(lst[:-1] ,lst[1:])]);
​
def share_digit(num , other):
  return any([d in str(other) for d in str(num)]);

