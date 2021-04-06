
def distance_to_nearest_vowel(txt):
  vwl,ml='aeiou',[]
  for i in range(len(txt)):
    if txt[i] in vwl:
      ml.append(0)
    else:
      counter=1
      while True:   
        if i+counter<len(txt) and txt[i+counter] in vwl or i-counter>=0 and txt[i-counter] in vwl:
          ml.append(counter)
          break
        else:
          counter+=1
  return ml

