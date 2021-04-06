
def reverse_image(image):
​
    return [[1 if element == 0 else 0 for element in part] for part in image]

