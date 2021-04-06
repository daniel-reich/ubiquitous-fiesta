
def count_smileys(lst):
  smiley_faces = [":)", ";)", ":-)", ":-D", ":~)", ":~D", ";-)", ";-D", ";~)", ";~D", ":D", ";D"]
  num_faces = 0
  for item in lst:
    if item in smiley_faces:
      num_faces += 1
  return num_faces

