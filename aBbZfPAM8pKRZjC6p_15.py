
def fruit_salad(fruits):
  fruit_chunks = []
  
  for fruit in fruits:
    fruit_len = len(fruit)
    chunk = fruit_len//2
    
    fruit_chunks.extend([fruit[:chunk], fruit[chunk:]])
    
  
  return ''.join(sorted(fruit_chunks))

