
def get_xp(d):
  sum = 0
  for key,val in d.items():
    if key == "Very Easy":
      pts = 5
    elif key == "Easy":
      pts = 10
    elif key == "Medium":
      pts = 20
    elif key == "Hard":
      pts = 40
    else:
      pts = 80
    sum = sum + pts*val
  return str(sum)+"XP"

