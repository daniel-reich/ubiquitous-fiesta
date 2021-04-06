
def constraint(s):                      # Constrained writting
  alphabet, s = "abcdefghijklmnopqrstuvwxyz", "".join([x.lower() for x in s if x.isalpha() or x==" "])
  is_pangram = lambda s: sorted(set("".join(s.split()))) == sorted(set(alphabet))
  is_heterogram = lambda s: len("".join(s.split()))==len(set("".join(s.split())))
  is_tautogram = lambda s: all(s.split()[i][0]==s.split()[i+1][0] for i in range(len(s.split())-1))
  is_transgram = lambda s: bool([set(x) for x in s.split()][0].intersection(*[set(x) for x in s.split()][1:]))
  return "Pangram" if is_pangram(s) else "Heterogram" if is_heterogram(s) else "Tautogram" if is_tautogram(s) else "Transgram" if is_transgram(s) else "Sentence"

