
def can_be_found(word,group):
  for g in group:
    if word.upper() in g:
      return True
    elif word[::-1].upper() in g:
      return True
  return False
​
def word_search(letters, words):
  lst = list(map(lambda x: ''.join(letters[x:8+x]),range(0,64,8)))
  lst.extend(list(map(lambda x: ''.join(letters[x:64:8]),range(0,8))))
  lst.extend(list(map(lambda x: ''.join(list(map(lambda y: letters[x+(9*y)],range(0,8-x)))),range(0,6))))
  lst.extend(list(map(lambda x: ''.join(list(map(lambda y: letters[8*x + 9*y],range(0,8-x)))),range(1,6))))
  lst.extend(list(map(lambda x: ''.join(list(map(lambda y: letters[x+(7*y)],range(0,x+1)))),range(2,8))))
  lst.extend(list(map(lambda x: ''.join(list(map(lambda y: letters[(8*x - 1) + 7*y],range(0,9-x)))),range(2,7))))
  
  for word in words:
    if can_be_found(word,lst) == False:
      return False
  return True

