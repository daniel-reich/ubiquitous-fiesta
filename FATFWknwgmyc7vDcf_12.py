
import re
def small_favor(sentence):
  months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october",
            "november", "december"]
  d0 = re.findall("\d\d/\d\d/\d\d", sentence)
  d1 = re.findall("\d\d\.\d\d\.\d\d", sentence)
  d2 = re.findall("\w+, \d\d\.\s\d\d", sentence)
  if d0:
    for i in d0:
      m, d, y = i.split("/")
      sentence = sentence.replace(i, "{}/{}/{}{}".format(m, d, 20 if int(y) < 25 else 19, y))
  if d1:
    for i in d1:
      m, d, y = i.split(".")
      sentence = sentence.replace(i, "{}.{}.{}{}".format(m, d, 20 if int(y) < 25 else 19, y))
  if d2:
    for i in d2:
      if i.split(",")[0].lower() in months:
        d, y = i.split(". ")
        sentence = sentence.replace(i, "{}. {}{}".format(d, 20 if int(y) < 25 else 19, y))
  return sentence

