
def XO(text):
  return len([char for char in text if char.lower() == 'o']) == len([char for char in text if char.lower() == 'x'])

