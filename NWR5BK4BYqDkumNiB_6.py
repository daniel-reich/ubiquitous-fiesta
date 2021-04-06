
import functools 
​
def digital_division(num): 
  results =  ["Indivisible",1,2, "Perfect"];
  digits  = get_digits(num);
  is_sum_div = num % sum(digits) == 0;
  prod = functools.reduce( lambda a, b : a*b  ,digits ,  1);
  is_prod_div  = prod > 0 and num % prod == 0;
  is_each_digit_div = all([d== 0 or num% d ==0 for d in digits ]);
  passed_tests  = sum([ is_each_digit_div, is_sum_div , is_prod_div]);
  return results[passed_tests];
  
def get_digits(num):
  return [int(d) for d in str(num)];

