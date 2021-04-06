
import re
def calc_bundled_temp(n, temp):
  temp = int(re.sub(r'\D+','',temp))
  def new_temp(n,temp):
    return "{}*C".format(str(round(temp,1))) if n == 0 else new_temp(n-1,(.1 * temp) + temp)
  return new_temp(n,temp)

