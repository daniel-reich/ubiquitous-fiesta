
def elasticize(word):
    l = len(word)
    final = ""
    if len(word) < 3:
        return word
        
    h = int(l//2)
    max = h+1
​
    front = word[:h]
    back = word[h+1:]
    for i in range(len(front)):
        a = i + 1
        f =  front[i]*(a)
        final += f
    
    if l % 2 != 0:
      b = max*word[h]
      final += b
    else:
      b = h*word[h]
      final += b
  
    for j in range(len(back)):
      if l % 2 == 0:
        ba = h - j - 1
      else:
        ba = h - j
      final += back[j]*(ba)
    return final

