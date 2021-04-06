
def word_builder(letters, positions):
  arr=[]
  for i in range(len(letters)):
    arr.append("-")
  for i in range(len(letters)):
    arr[positions[i]]=letters[i]
  new=""
  for i in arr:
    new+=i
  return new

