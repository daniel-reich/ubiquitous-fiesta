
def bird_code(lst):
  num_of_letters = ([4], [2, 2], [1, 1, 2], [1, 1, 1, 1])
  code_lst = []
  for bird in lst:
    first_letter_index = [i for i in range(len(bird)) if bird[i].isupper()]
    num_of_words = len(first_letter_index)
    code = ""
    for i in range(num_of_words):
      start = first_letter_index[i]
      end = start + num_of_letters[num_of_words - 1][i]
      code += bird[start: end]
    code_lst.append(code.upper())
  return code_lst

