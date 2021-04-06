
def sigilize(desire):
  arr = [i for i in desire.upper()[::-1] if i not in "AEIOU" and i !=" "]
  arr1 = [];
  [arr1.append(i) for i in arr if i not in arr1]
  return "".join(arr1[::-1])

