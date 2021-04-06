
def blah_blah(txt, n):
  txt_lst = txt.split()[::-1]
  for txt in range(len(txt_lst)):
    if txt == 0:
      txt_lst[txt] = "blah..."
      continue
    if txt > n - 1:
      break
    txt_lst[txt] = "blah"
  return " ".join(txt_lst[::-1])

