
def calc_diff(obj, limit):
  i=0
  for key,value in obj.items():
    i+=value
  a=i-limit
  return a
print(calc_diff({"skate": 200, "painting": 200, "shoes": 1 }, 400))

