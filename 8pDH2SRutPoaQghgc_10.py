
def relation_to_luke(name):
  sentence = "Luke, I am your "
  if name == "Darth Vader":
    sentence += "father."
  elif name == "Leia":
    sentence += "sister."
  elif name == "Han":
    sentence += "brother in law."
  elif name == "R2D2":
    sentence += "droid."
  return sentence

