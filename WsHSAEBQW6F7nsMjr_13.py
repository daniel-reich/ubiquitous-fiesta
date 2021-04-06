
import statistics
​
def flatten_the_curve(lst):
  try :
    mean = statistics.mean(lst)
    return [round(mean,1) for x in lst]
  except:
    return []

