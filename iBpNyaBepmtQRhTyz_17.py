
def c_cipher(msg, keyword):
  def encode_or_decode(msg):
    uppercase = list('abcdefghijklmnopqrstuvwxyz'.upper())
    
    for l8r in uppercase:
      if l8r in msg:
        return 'E'
    
    if ' ' in msg:
      return 'E'
    
    return 'D'
  class Cipher:
​
    def __init__(self, key):
      self.key = key
    
    def encrypt(self, msg):
​
      msg = msg.lower()
      to_remove = list('.,!?/')
​
      for item in to_remove:
        if item in msg:
          msg = msg.replace(item, '')
      
      msg = ''.join(msg.split())
      print(msg)
      columns = {}
​
      count = 0
​
      for n in range(len(msg)):
        l8r = msg[n]
        if self.key[count] not in columns.keys():
          columns[self.key[count]] = [l8r]
        else:
          columns[self.key[count]].append(l8r)
        count += 1
        if count >= len(self.key):
          count = 0
      
      values = {}
      a = list('abcdefghijklmnopqrstuvwxyz')
​
      for n in range(len(a)):
        l8r = a[n]
        if l8r in self.key:
          values[n] = l8r
      
      goal_length = max([len(l) for l in list(columns.values())])
​
      for column in columns.keys():
        col = columns[column]
        while len(col) < goal_length:
          col.append('x')
        columns[column] = col
      
      new_order = []
​
      for value in sorted(list(values.keys())):
        ident = values[value]
        new_order.append(''.join(columns[ident]))
      
      return ''.join(new_order)
​
    def decrypt(self, msg):
​
      msg = list(msg)
      len_of_columns = int(len(msg) / len(self.key))
​
      columns = []
​
      for n in range(len(self.key)):
        column = []
        for num in range(len_of_columns):
          column.append(msg[0])
          msg.pop(0)
        columns.append(column)
      
      l8r_vals = {}
      a = list('abcdefghijklmnopqrstuvwxyz')
​
      for n in range(26):
        l8r = a[n]
        if l8r in self.key:
          l8r_vals[n] = l8r
      
      column_id = {}
      index = 0
​
      for val in sorted(list(l8r_vals.keys())):
        column_id[l8r_vals[val]] = columns[index]
        index += 1
      
      rows = []
​
      for n in range(len_of_columns):
        row = []
        for val in self.key:
          col = column_id[val]
          row.append(col[n])
        rows.append(''.join(row))
      
      return ''.join(rows)
​
  cipher = Cipher(keyword)
​
  eod = encode_or_decode(msg)
​
  if eod == 'E':
    return cipher.encrypt(msg)
  elif eod == 'D':
    return cipher.decrypt(msg)
  else:
    return 'EOD error! {}'.format(eod)

