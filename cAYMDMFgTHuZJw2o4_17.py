
def reverse_image(image):
  for i in range(len(image)):
    for j in range(len(image[0])):
      image[i][j] = 2+~image[i][j]
  return image

