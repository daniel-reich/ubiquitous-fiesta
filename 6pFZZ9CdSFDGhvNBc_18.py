
import numpy as np
def factor_group(num):
  if np.sqrt(num)*10**len(str(num))%10==0:
    return 'odd'
  else:
    return 'even'

