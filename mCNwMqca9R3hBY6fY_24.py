
def make_happy(txt):
  faces={
    ":(" : ":)",
    "8(" : "8)",
    "x(" : "x)",
    ";(" : ";)"
  } 
  for old,new in faces.items():
    txt= txt.replace(old,new)
  return txt

