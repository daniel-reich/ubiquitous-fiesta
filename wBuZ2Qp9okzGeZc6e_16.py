
def first_place(road):
  flip = reversed(road)
  for letter in flip:
    if letter.isalpha():
      return letter

