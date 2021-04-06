
def same_letter_pattern(txt1, txt2):
  def unique_letter_location (strings):
    x = []
    for i in strings:
      if i not in x:
        x.append(i)
      else:
        continue
    y = list(range(1,len(x)+1))
    legend = dict(zip(x,y))
    pattern = ''.join([str(legend[i]) for i in strings])
    return pattern
  return unique_letter_location(txt1) == unique_letter_location(txt2)

