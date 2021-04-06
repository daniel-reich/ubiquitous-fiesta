
def increment_string(s):
    a = ""
    s_yedek = s
    while s_yedek[-1].isdigit():
      a = s_yedek[-1]+a
      s_yedek = s_yedek[:-1]
    if a != "":
      sayi = int(a)+1
    else:
      sayi = 1
    if len(a) >= len(str(sayi)):
      s = s[:-(len(str(sayi)))]+str(sayi)
    elif a == "":
      s = s + str(sayi)
    else:
      s = s[:len(a)]+str(sayi)
    return s

