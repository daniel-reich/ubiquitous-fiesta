
def relation_to_luke(name):
  family = {"Darth Vader": "father", "Leia": "sister", "Han": "brother in law", "R2D2": "droid"
}
  for k,v in family.items():
    if k == name:
      msg = "Luke, I am your " + v + "."
      return msg

