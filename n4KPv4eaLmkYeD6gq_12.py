
def face_interval(num):
  if type(num) != list:
    return ':/'
  largest = max(num)
  smallest = min(num)
  interval = largest - smallest
  if interval in num:
    return ':)'
  else:
    return ':('

