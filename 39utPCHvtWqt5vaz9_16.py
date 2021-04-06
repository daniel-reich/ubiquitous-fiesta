
def direction(lst):
  results = [] #creat empty list to hold results
  for each in lst: #iterate through each elemnt in lst
    new = '' #create an empty container for new string
    for i in each: #iterate through each character in the string
      if i == 'e':
        i_new = 'w'
      if i == 'a':
        i_new = 'e'
      if i == 's':
        i_new = 's'
      if i == 't':
        i_new = 't'
      if i == 'E':
        i_new = 'W'
      if i == 'A':
        i_new = 'E'
      if i == 'S':
        i_new = 'S'
      if i == 'T':
        i_new = 'T'
      if i == ' ':
        i_new = ' '
      new += i_new#add the new character to the return string
    results.append(new) #add the new string to the results list
  return results #return results

