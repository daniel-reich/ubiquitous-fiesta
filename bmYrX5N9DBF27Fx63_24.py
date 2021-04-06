
import numpy as np
def greatest_impact(lst):
  w,ml,s,format_=[],[],[],['Weather', 'Meals', 'Sleep']
  for el in lst:
    w.append(el[1]/10),ml.append(el[2]/3),s.append(el[3]/10)
  max_var =max([np.std(w),np.std(ml),np.std(s)])
  return 'Nothing' if max_var== 0 else format_[[np.std(w),np.std(ml),np.std(s)].index(max_var)]

