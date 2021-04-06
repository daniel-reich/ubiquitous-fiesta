
def reverse_image(image):
   
   final = [[0 if (k==1 ) else 1 if (k == 0 ) else "zero" for k in j] for j in image]
   return (final)

