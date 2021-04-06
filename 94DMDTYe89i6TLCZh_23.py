
def get_languages(num):
  langs = ["C#", "C++", "Java", "JavaScript", "PHP", "Python", "Ruby", "Swift"]
  final = []
  bin_str = bin(num)[2:]
  bin_num = int(bin_str, 2)
  for i in range(len(langs)):
    if bin_num & (1 << i):
      final.append(langs[i])
  return final

