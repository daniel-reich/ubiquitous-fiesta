
def text_to_number_binary(txt):
  lst = txt.split()
  lst = ["0" if x.lower() == "zero" else x for x in lst]
  lst = ["1" if x.lower() == "one" else x for x in lst]
  lst = [x for x in lst if x == '0' or x == '1']
  res = "".join(lst)
  desired_len = 8 * (len(res) // 8)
  return res[:desired_len]

