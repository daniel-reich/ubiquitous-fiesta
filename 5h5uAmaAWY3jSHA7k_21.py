
import numpy as np
def landscape_type(lst):
  
  skyline = 'neither'
  
  # First try with mountain shape
  extreme = max(lst)
  ixtreme = lst.index(extreme)
​
  lstcpy = list.copy(lst)
  lstcpy.remove(extreme)
​
  if ixtreme != 0 and ixtreme != lst.__len__()-1 and extreme not in lstcpy:
    dlst = list(np.diff(lst))
    imaxincr = dlst.index(max(dlst))
    if any(np.array(dlst)[0:imaxincr] < 0) == True:
        skyline = 'neither'
    else:
        skyline = 'mountain'
  else:
    # If not, try with valley shape
    extreme = min(lst)
    ixtreme = lst.index(extreme)
​
    lstcpy = list.copy(lst)
    lstcpy.remove(extreme)
    
    if ixtreme != 0 and ixtreme != lst.__len__()-1 and extreme not in lstcpy:
        skyline = 'valley'
    else:
        skyline = 'neither'
​
  return skyline

