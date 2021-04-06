
def seq_level(lst): 
  f_d = [lst[i]-lst[i-1] for i in range(1,len(lst))]
  s_d = [f_d[i]-f_d[i-1] for i in range(1,len(f_d))]
  t_d = [s_d[i]-s_d[i-1] for i in range(1,len(s_d))]
​
​
  return "Linear" if len(set(f_d)) == 1 else "Quadratic" if len(set(s_d)) == 1 else "Cubic"

