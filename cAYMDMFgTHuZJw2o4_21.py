
def reverse_image(image):
  result =[]
  for elem in image:
    l = []
    for n in elem:
      if n == 1:
        l.append(0)
      else:
        l.append(1)
    result.append(l)
  return result

