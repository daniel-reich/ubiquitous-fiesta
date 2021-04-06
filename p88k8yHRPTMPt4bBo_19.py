
def count_vowels(txt):
  vowels = {'a', 'e', 'i', 'o', 'u'}
           
  v_count = 0
  
  for char in txt:
    if char in vowels:
      v_count+=1
      
  return v_count

