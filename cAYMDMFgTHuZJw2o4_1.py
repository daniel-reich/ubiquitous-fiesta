
def reverse_image(image):
  return [[int(not(x)) for x in val] for val in image]

