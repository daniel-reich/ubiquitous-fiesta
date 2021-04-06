
import numpy as np
def crop_hydrated(field):
  field = np.array(field) == 'w'
  watered = 0 * field
  for i,j in np.ndindex(field.shape):
    if field[i,j]:
      for u,v in np.ndindex((3,3)):
        try: watered[i+u-1,j+v-1] = 1
        except: pass
  
  return np.sum(watered == 0) == 0

