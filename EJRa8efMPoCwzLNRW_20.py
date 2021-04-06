
def dakiti(txt):
  raw_txt = [i for i in txt.split(" ")]
  sqed_txt = []
  for i in raw_txt:
    for j in range(len(i)):
      try: t = int(i[j])
      except ValueError:
        continue
      else:
        frac = []
        for y in i:
          try: x = int(y)
          except ValueError: frac.append(y)
          string = ""
          for z in frac:
            string += z
        sqed_txt.append([int(i[j]),string])
  semi_final = sorted(sqed_txt)
  final = ""
  for i in range(len(semi_final)):
    if i != len(semi_final)-1:
      final += semi_final[i][1] + " "
    else:
      final += semi_final[i][1]
  return final

