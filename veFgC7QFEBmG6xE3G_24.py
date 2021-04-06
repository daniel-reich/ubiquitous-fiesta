
def is_smooth(sentence):
  arr = sentence.split(' ')
  for x in range(len(arr)-1):
    if arr[x][-1] != arr[x+1][0].lower():
      return False
  return True

