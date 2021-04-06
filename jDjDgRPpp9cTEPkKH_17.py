
def over_time(lst):
  std, ot =  (17-lst[0]) * lst[2] if lst[1] >= 17 and lst[0] < 17 else (lst[1] - lst[0]) * lst[2] if lst[0] < 17 else 0, ((lst[1] - 17) * lst[2] * lst[3]) if (lst[1] - 17) > 0 and lst[0] < 17 else (lst[1] - lst[0]) *lst[2]*lst[3] if lst[0] >= 17 else 0
  pay = "$"+str(round(float(std+ot+.001),2))
  if pay[-2] == ".": pay += "0" 
  return pay

