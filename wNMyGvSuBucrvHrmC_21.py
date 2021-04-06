
def only_consists_of_substring(string, substring):
  count = len(string) // len(substring)
  mult_string = substring * count
  return mult_string == string
​
def number_of_repeats(string):
  for i in range(1, len(string) + 1):
    substring = string[:i]
    result = only_consists_of_substring(string, substring)
    if result == True:
      return len(string) // len(substring)

