
def get_languages(num):
  d = {0: 'C#', 1: 'C++', 2: 'Java', 3: 'JavaScript', 4: 'PHP', 5: 'Python', 6: 'Ruby', 7: 'Swift'}
  return [d[i] for i in range(8) if num & 2**i]

