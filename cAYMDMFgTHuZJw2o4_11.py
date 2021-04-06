
def reverse_image(image):
  lst = []
  for i in image:
    lst += [[1 if j == 0 else 0 for j in i]]
  return lst

