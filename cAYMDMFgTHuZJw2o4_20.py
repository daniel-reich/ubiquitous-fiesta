
def reverse_list(lst):
  return [abs(x-1) for x in lst]
def reverse_image(image):
  return [reverse_list(x) for x in image]

