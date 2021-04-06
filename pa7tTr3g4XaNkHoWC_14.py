
def pig_latin_sentence(s):
  b = []
  a = s.split()
  for i in a:
      if i[0] in "aeiou":
         b.append(i+"way")
      else:
          for j in range(len(i)):
              if i[j] in "aeiou":
                  b.append(i[j:]+i[:j]+"ay")
                  break
  return " ".join(b)

