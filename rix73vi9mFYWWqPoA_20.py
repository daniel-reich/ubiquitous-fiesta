
def record_temps(records, current_week):
  zipped = zip(records, current_week)
  lst = [record + current for record, current in zipped]
  return [[min(element), max(element)] for element in lst]

