
def edabit_in_string(txt):
      pos = 0
      b = "edabit"
      for ch in txt:
            if pos < len(b) and ch == b[pos]:
                  pos += 1
      return 'NO' if not pos == len(b) else 'YES'

