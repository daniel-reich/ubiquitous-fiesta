
import re
​
def c_cipher(msg, keyword):
  if ' ' in msg:
    msg = re.sub(r'[^\w]','',msg).lower()
    rows = [msg[i:i+len(keyword)] for i in range(0,len(msg),len(keyword))]
    if len(rows[-1]) != len(keyword):
      rows[-1] += 'x' * (len(keyword) - len(rows[-1]))
    table = {a: ''.join(r[i] for r in rows) for i, a in enumerate(keyword)}
    return ''.join(table[a] for a in sorted(keyword))
  else:
    col_len = len(msg) // len(keyword)
    cols = [msg[i:i+col_len] for i in range(0,len(msg),col_len)]
    table = {a: cols[i] for i, a in enumerate(sorted(keyword))}
    ord_cols = [table[letter] for letter in keyword]
    return ''.join(''.join(col[i] for col in ord_cols) for i in range(len(ord_cols[0])))

