
def get_languages(num):
    keys = ['Swift', 'Ruby', 'Python', 'PHP', 'JavaScript', 'Java', 'C++', 'C#']
    lan = {'Swift': 128, 'Ruby':64, 'Python':32,
            'PHP': 16, 'JavaScript': 8,
            'Java': 4, 'C++': 2,  'C#': 1
          }
​
    result = {}
​
    for key in keys:
      if num - sum(result.values()) >= lan[key]:
        result[key] = lan[key]
​
    return sorted(result)

