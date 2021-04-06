
def letter_check(lst):
  srt1 = sorted(lst[0].lower())
  srt2 = sorted(lst[1].lower())
  print(srt1)
  print(srt2)
  for chr in srt1:
    if chr not in srt2:
      srt1.remove(chr)
  return srt1 == srt2

