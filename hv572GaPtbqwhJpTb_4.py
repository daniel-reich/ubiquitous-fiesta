
def elasticize(word):
  if len(word) % 2 == 0:
    left, right = word[:len(word)//2], word[len(word)//2:]
  else:
    left, right = word[:len(word)//2+1], word[len(word)//2+1:]  
  return "".join([left[x] * (x + 1) for x in range(len(left))]) + "".join([right[x] * abs(x-len(right)) for x in range(len(right))])

