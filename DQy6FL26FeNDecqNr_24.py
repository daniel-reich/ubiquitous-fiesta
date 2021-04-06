
def correct_stream(user, correct):
  output=[]
  for x in range(len(user)):
    if user[x]==correct[x]:
      output.append(1)
    else:
      output.append(-1)
  return output

