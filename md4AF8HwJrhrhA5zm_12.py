
def colour_harmony(anchor, combination):
  def combinations(ap, comb):
    def comp(p):
      n = p + 6
​
      if n >= 12:
        n -= 12
      
      return n
    def anal(p):
      m = p - 1
      pl = p + 1
​
      if m < 0:
        m += 12
      if pl >= 12:
        pl -= 12
​
      return [m, pl]
    def tria(p):
      pos = p + 4
      neg = p - 4
​
      if pos >= 12:
        pos -= 12
      if neg < 0:
        neg += 12
      
      return [neg, pos]
    def s_comp(p):
      cp = comp(p)
​
      neg = cp - 1
      pos = cp + 1
​
      if neg < 0:
        neg += 12
      if pos >= 12:
        pos += 12
      
      return neg, pos
    def rect(p):
      def short(p):
        op = p + 2
        return op
      def lon(p):
        l = p + 4
        return l
      
      p2 = short(p)
      p3 = lon(p2)
      p4 = short(p3)
​
      points = [p2, p3, p4]
      np = []
​
      for point in points:
        if point >= 12:
          np.append(point - 12)
        elif point < 0:
          np.append(point + 12)
        else:
          np.append(point)
      
      return np
    def squa(p):
      def side(p):
        return p + 3
      
      sides = [p]
​
      for number in range(0, 3):
        np = side(sides[-1])
        if np >= 12:
          np -= 12
        if np < 0:
          np += 12        
        sides.append(np)
      
      sides.pop(0)
​
      return sides
    
    if comb == 'triadic':
      r = tria(ap)
    elif comb == 'complementary':
      r = comp(ap)
    elif comb == 'square':
      r = squa(ap)
    elif comb == 'analogous':
      r = anal(ap)
    elif comb == 'rectangle':
      r = rect(ap)
    elif comb == 'split_complementary':
      r = s_comp(ap)
    
    return r
  
​
  colours = ["red", "red-orange", "orange", "yellow-orange", "yellow", "yellow-green",  "green", "blue-green", "blue", "blue-violet", "violet", "red-violet"]
  colour_idents = range(0, len(colours))
  colour_dic = {}
​
  for number in colour_idents:
    colour = colours[number]
    colour_dic[colour] = number
  
  appos = colour_dic[anchor.lower()]
​
  comb = combinations(appos, combination)
​
  final_colours = set()
​
  final_colours.add(colours[appos])
​
  t = isinstance(comb, int)
​
  if t == False:
    for pos in comb:
      colour = colours[pos]
      final_colours.add(colour)
​
  elif t == True:
    final_colours.add(colours[comb])
  
  return final_colours

