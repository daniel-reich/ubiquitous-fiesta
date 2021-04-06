
def index_of_caps(word):
  list_of_caps = [];
  
  for i in range(len(word)):
    if (str.isupper(word[i])):
      list_of_caps.append(i);
      
  return list_of_caps;

