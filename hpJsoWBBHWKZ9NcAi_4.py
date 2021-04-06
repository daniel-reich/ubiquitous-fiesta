
def bird_code(lst):
  result = []
  for bird in lst:
      words = [word.upper() for word in bird.replace('-', ' ').split()]
      size = len(words)
      if size == 4:
          name = ''.join(i[0] for i in words)
      elif size == 3:
          name = words[0][0] + words[1][0] + words[2][:2]
      elif size == 2:
          name = words[0][:2] + words[1][:2]
      else:
          name = words[0][:4]
      result.append(name)
  return result

