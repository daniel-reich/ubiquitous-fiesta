
def reverse_image(image):
  for i in range(len(image)):
    for j in range(len(image[i])):
      if image[i][j] == 0:
        image[i][j] = 1
      else:
        image[i][j] = 0
  return image

