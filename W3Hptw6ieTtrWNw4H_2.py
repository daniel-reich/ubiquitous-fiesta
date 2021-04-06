
def bifid(text):
  def polybius_square(txt, c):#My code from the first Polybius Square 
    def encrypt(txt, rows, cols):
      
      a = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.upper().split()
      encrypted = ''
      
      for l8r in txt:
        if l8r in a:
          if l8r == 'J':
            l8r = 'I'
​
          row = None
          col = None
          
          for n in range(1, 6):
            rowtest = rows[n]
            coltest = cols[n]
​
            if l8r in rowtest:
              row = n
            if l8r in coltest:
              col = n
            
            if row != None and col != None:
              break
          
          if row == None:
            return 'error finding row'.upper()
          if col == None:
            return 'error finding col'.upper()
​
          el8r = '{r}{c}'.format(r = row, c = col)
​
          encrypted += el8r
        else:
          if l8r == ' ':
            encrypted += l8r
      
      return encrypted
    def decrypt(cipher, rows, cols):
​
      words = cipher.split()
​
      unencrypted_words = []
​
      for word in words:
​
        w = ''
​
        for n in range(0, len(word), 2):
          
          rowid = int(word[n])
          colid = int(word[n + 1])
​
          row = rows[rowid]
          col = cols[colid]
​
          for letter in row:
            if letter in col:
              l8r = letter
              break
          
          w += l8r
​
        unencrypted_words.append(w)
      
      unencrypted = ' '.join(unencrypted_words)
​
      return unencrypted.lower()
    
    rows = {1: 'A B C D E'.split(), 2: 'F G H I K'.split(), 3: 'L M N O P'.split(), 4: 'Q R S T U'.split(), 5: 'V W X Y Z'.split()}
    cols = {}
​
    for n in range(0, 5):
      col = []
      for num in range(1, 6):
        row = rows[num]
        item = row[n]
        col.append(item)
      cols[n + 1] = col
    
    if c == 'E':
      tr = encrypt(txt.upper(), rows, cols)
    elif c == 'D':
      tr = decrypt(txt, rows, cols)
    else:
      return 'UNKNOWN ERROR!!!'
​
    return tr
  def b_encode(square):
​
​
    row1 = []
    row2 = []
​
    for n in range(0, len(square), 2):
      row1.append(int(square[n]))
      row2.append(int(square[n + 1]))
    
    new_l8rs = []
    rows = row1
​
    for item in row2:
      rows.append(item)
    del row2
    del row1
​
    
    for n in range(0, len(rows), 2):
      
      n1 = rows[n]
      n2 = rows[n + 1]
​
      l8r = '{}{}'.format(n1, n2)
​
      new_l8rs.append(l8r)
    
    return ''.join(new_l8rs)
  def b_decode(square):
​
    rows = square
​
    half = len(square) / 2
​
    row1 = []
    row2 = []
​
    for n in range(0, len(square)):
      item = rows[n]
      if n < half:
        row1.append(item)
      else:
        row2.append(item)
    
    if len(row1) != len(row2):
      return 'ERROR'
    
    decoded = []
    for n in range(0, len(row1)):
​
      r1 = row1[n]
      r2 = row2[n]
​
      d = r1 + r2 
​
      decoded.append(d)
    
    return ''.join(decoded)
  def choose(txt, a):
​
    to_do = 'D'
  
    for item in txt:
      if item not in a:
        to_do = 'E'
        break
​
    return to_do
​
  
  txt = ''
  a = 'a b c d e f g h i k l m n o p q r s t u v w x y z'.split()
  c = choose(text, a)
  
  for item in text:
    if item in a or item.lower() in a:
      txt += item.lower()
    else:
      try:
        test = int(item)
        txt += item
      except ValueError:
        continue
  del text
​
  
  ps = polybius_square(txt, 'E')
  
  if c == 'E':
    be = b_encode(ps)
  elif c == 'D':
    be = b_decode(ps)
  else:
    return 'UNKNOWN ERROR'
    
  ps2 = polybius_square(be, 'D')
​
  return ps2

