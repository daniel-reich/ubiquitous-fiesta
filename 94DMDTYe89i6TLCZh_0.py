
def get_languages(num):
  languages = [ "C#", "C++", "Java", "JavaScript", "PHP", "Python", "Ruby", "Swift" ]
  return [languages[i] for i in range(8) if num & (1 << i)]

