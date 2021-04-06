
import math
def free_throws(success, rows):
  prob = math.pow(float(success.strip("%")),rows)/(math.pow(100,rows))
  strp = round(prob*100)
  return str(strp)+"%"

