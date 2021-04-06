
def reverse_image(image):
  for row, rows in enumerate(image):
    for col, num in enumerate(rows):
      image[row][col] = 0 if num>0 else 1 
  return image

