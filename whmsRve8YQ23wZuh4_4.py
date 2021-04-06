
def sort_dates(arr, mode):                      # Sort the sort_dates
  """ Given a mode [ascending or descending], sort the times DD-MM-YYYY_HH:MM """
​
  arr = " ".join(arr).replace("_","-").replace(":","-").split()
  for i, x in enumerate(arr):
    arr[i] = x.split("-")
  arr = sorted(sorted(sorted(sorted(sorted(arr, key = lambda x: x[4]), key = lambda x: x[3]), key = lambda x: x[0]), key = lambda x: x[1]), key = lambda x: x[2]) if mode=="ASC" else sorted(sorted(sorted(sorted(sorted(arr, key = lambda x: x[4]), key = lambda x: x[3]), key = lambda x: x[0]), key = lambda x: x[1]), key = lambda x: x[2])[::-1]
  return ["-".join(x[0:3]) + "_" + x[3] + ":" + x[4] for x in arr]

