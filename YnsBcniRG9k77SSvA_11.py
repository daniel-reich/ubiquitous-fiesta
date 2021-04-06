
def print_all_groups():
  grades = ['1','2','3','4','5', '6'] 
  letters = ['a','b','c','d','e']
  output = []
  
  for grade in grades:
    for letter in letters:
      output.append(grade+letter)
​
  output = ', '.join(output)
​
  return(output)

