
def get_languages(n):
  return [["C#", "C++", "Java", "JavaScript", "PHP", "Python", "Ruby", "Swift"][i] for i, x in enumerate(bin(n)[2:][::-1]) if x == "1"]

