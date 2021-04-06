
def get_languages(num):
  languages = ["C#", "C++", "Java", "JavaScript", "PHP", "Python", "Ruby", "Swift"]
  proficient = []
  for language in languages[::-1]:
    if 2 ** languages.index(language) <= num:
      proficient.append(language)
      num -= 2 ** languages.index(language)
    if num < 0:
      proficient.pop()
      break
  return sorted(proficient)

