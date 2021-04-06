
def reverse_image(image):
  for x in range(len(image)):
    for y in range(len(image[x])):
      image[x][y] = image[x][y] ^ 1
  return image

