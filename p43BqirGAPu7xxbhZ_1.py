
def diamond(carat):
  def good_or_perfect(l):
    if l%2 == 0:
      return 'good cut'
    else:
      return 'perfect cut'
  
  class Diamond:
​
    def __init__(self, carat):
      self.c = carat
      self.cut = good_or_perfect(carat)
​
      if self.cut == 'good cut':
        self.rnum = carat - 1
        self.cnum = carat
      else:
        self.rnum = carat
        self.cnum = carat
​
      self.cols = []
​
      def make_half(rowlen, collen):
        half = int(rowlen/2) + 1
        rows = []
        index = 0
        for n in range(half):
          row = []
          first = False
          for num in range(collen):
            if first == False:
              if num == index:
                row.append(1)
                index += 1
                first = True
              else:
                row.append(0)
            else:
              if num == collen - index:
                row.append(1)
              else:
                row.append(0)
          rows.append(row)
        
        return rows
      
      half_rows = make_half(self.rnum, self.cnum)
​
      self.rows = list(reversed(half_rows[1:])) + half_rows
      
      for n in range(self.cnum):
        col = []
        for row in self.rows:
          col.append(row[n])
        self.cols.append(col)
​
  d = Diamond(carat)
​
  return [d.rows, d.cut]

