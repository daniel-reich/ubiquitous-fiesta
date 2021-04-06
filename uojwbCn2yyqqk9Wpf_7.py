
def is_untouchable(num):
  global d
  if num<2:return "Invalid Input"
  for i in range(len(d),num*num+1):
    d[i]=sum_factor(i)
  return [i for i in range(num,num*num+1) if d[i]==num] or True
    
def sum_factor(n):
    res = 1;mem=n
    for i in range(2, int(n**0.5 + 1)):
        curr_sum = 1
        curr_term = 1
        while n % i == 0:
            n = n / i;
            curr_term = curr_term * i;
            curr_sum += curr_term;
        res = res * curr_sum 
    if n > 2:
        res = res * (1 + n) 
    return int(abs(res - mem))
  
d={i:sum_factor(i) for i in range(36000)}

