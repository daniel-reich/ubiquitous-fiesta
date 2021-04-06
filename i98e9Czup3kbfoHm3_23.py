
def text_to_number_binary(txt):
  txt = txt.lower().split(" ")
  txt = [i for i in txt if i in ["zero", "one"]]
  if (len(txt) - (len(txt) % 8)) % 8 != 0:
      return ""
​
  txt = "".join(txt[:(len(txt) - (len(txt) % 8))]).replace("zero", "0").replace("one", "1")
  return txt

