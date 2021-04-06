
def split_bunches(bunches):
  result_array = []
  for item in bunches:
    for i in range(int(item["quantity"])):
      result_array.append({"name" : item["name"], "quantity" : 1})
      
  return result_array

