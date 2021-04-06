
def organize(txt):
  try:
    name, age, occupation = txt.split(', ')
    return {
      'name': name,
      'age': int(age),
      'occupation': occupation
    }
  except ValueError:
    return {}

