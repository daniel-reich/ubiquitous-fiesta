
def avg_note(students):
  adict = {}
  newlist = []
  for eachstudent in students:
    adict['name'] = eachstudent['name']
    try:
      adict['avgNote'] = round(sum(eachstudent['notes']) / len(eachstudent['notes']))
    except ZeroDivisionError as zero_err:
      adict['avgNote'] = 0
    newlist.append(adict)
    adict = {}
  return newlist

