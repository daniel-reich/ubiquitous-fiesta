
NUM_DICT = {"abc": "2", "def": "3", "ghi": "4", "jkl": "5", "mno": "6", "pqrs": "7", "tuv": "8", "wxyz": "9"}
def dial(txt):
  return_txt = ""
  for ch in txt:
    if ch.isdigit():
      return_txt += ch
    elif ch.isalpha():
      for key in NUM_DICT.keys():
        if ch.lower() in key:
          return_txt += NUM_DICT[key]
    else:
      return_txt += ch
  return return_txt

