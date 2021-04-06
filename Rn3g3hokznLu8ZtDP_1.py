
def increment_string(txt):
  numlst = []
  end = 0
  for i in range(len(txt) - 1, 0, -1):
    try:
      val = int(txt[i])
      numlst.append(str(val))
    except ValueError:
      end = i + 1
      break
  txt = txt[:end]
  numlst.reverse()
  numlen = len(numlst)
  num = str(1 if numlen == 0 else int("".join(numlst)) + 1)
  num = "0" * (numlen - len(num)) + num
  return txt + num

