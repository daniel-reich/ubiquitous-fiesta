
langs = ['C#', 'C++', 'Java', 'JavaScript', 'PHP', 'Python', 'Ruby', 'Swift']
def get_languages(num):
  return [lang for i, lang in enumerate(langs) if num & (1 << i)]

