
def flip(txt, spec):
  txt_list = txt.split()
  if spec == "word":
    backwards_word_list = []
    for word in txt_list:
      backwards_word_list.append(word[::-1])
    return " ".join(backwards_word_list)
  if spec == "sentence":
    backwards_list = []
    for word in reversed(txt_list):
      backwards_list.append(word)
    return " ".join(backwards_list)

