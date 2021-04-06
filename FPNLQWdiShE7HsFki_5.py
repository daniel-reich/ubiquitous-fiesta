
class Insect:
  def __init__(self,insect):
    self.letter = insect[0]
    self.number = int(insect[1])
  def next_letter(self):
    return "A" if self.letter == "H" else chr(ord(self.letter)+1)
  def prev_letter(self):
    return "H" if self.letter == "A" else chr(ord(self.letter)-1)
  
def spider_vs_fly(spider, fly):
  s = Insect(spider)
  f = Insect(fly)
  lst = [spider]
  if s.number > f.number:
    lst.extend(list(map(lambda x: s.letter + str(x),range(s.number-1,f.number-1,-1))))
  if s.next_letter() != f.letter and s.prev_letter() != f.letter:
    if s.next_letter() == f.prev_letter():
      lst.append(s.next_letter() + str(f.number))
    elif s.prev_letter() == f.next_letter():
      lst.append(s.prev_letter() + str(f.number))
    else:
      if f.number > 1:
        lst.extend(list(map(lambda x: s.letter + str(x),range(f.number-1,0,-1))))
      lst.append("A0")
      if f.number > 1:
        lst.extend(list(map(lambda x: f.letter + str(x),range(1,f.number))))
  lst.append(fly)
  return '-'.join(lst)

