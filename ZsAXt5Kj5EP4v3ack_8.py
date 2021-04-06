
def secret(txt):
  import collections
  digits = collections.Counter(txt)["$"]
  txt_split = [txt.split(">")[0]]
  txt_split.append(txt.split(">")[1].split(".")[0])
  txt_split.append(txt.split(".")[1].split("$")[0])
  txt_split.append(txt.split("*")[1])
  first_tag_name = txt_split[0]
  repeat_tag_name = txt_split[1]
  class_lead_letter = txt_split[2]
  repeats = int(txt_split[3])
  output = "<"+first_tag_name+">"
  closing_tag = "<"+"/"+repeat_tag_name+">"
  for i in range(1,repeats+1):
    output += "<" + repeat_tag_name + " class='" + class_lead_letter + "0"*(digits-len(str(i))) + str(i) + "'>" + closing_tag
  output += "<"+"/"+first_tag_name+">"
  return output

