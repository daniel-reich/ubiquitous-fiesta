
def wurst_is_better(txt):
  german = [ "Bratwurst", "Kochwurst", "Leberwurst", "Mettwurst", "Rostbratwurst"]
  non_german = [ "Kielbasa", "Chorizo", "Moronga", "Salami", "Sausage", "Andouille", "Naem", "Merguez", "Gurka", "Snorkers", "Pepperoni"]
  #ed_germans = [i.lower()+"s" for i in german]
  ed_non_germans = [i.lower()+"s" for i in non_german]
  ed_german = [i.lower() for i in german]
  ed_non_german = [i.lower() for i in non_german]
​
  return " ".join([i if i.lower() in ed_german else "Wurst" if i.lower() in ed_non_german else "Wursts" if i.lower() in ed_non_germans else i for i in txt.split() ])

