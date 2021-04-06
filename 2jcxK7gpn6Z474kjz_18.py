
def security(txt):
  for item in txt.split('G'):
    if 'T' in item and '$' in item :
      return "ALARM!"
  return "Safe"

