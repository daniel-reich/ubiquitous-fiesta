
def rotate_by_one(arr):
  first_elem = arr.pop(-1)
  arr2 = list(arr)
  arr2.insert(0,first_elem)
  return arr2

