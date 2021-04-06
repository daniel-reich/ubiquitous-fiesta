
def percentage_happy(numbers):
  happy_nums  = sum([numbers[idx] in adjacent(idx , numbers) for idx in range(0 , len(numbers))]);
  return round(happy_nums/len(numbers) , 1);
​
def adjacent(idx , lst):
  return [lst[idx+1]] if  idx  == 0 else [lst[idx-1]] if idx == len(lst) - 1 else [lst[idx-1] , lst[idx+1]];

