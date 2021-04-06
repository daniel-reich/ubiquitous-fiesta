
def validate_email(txt):
  passed = {"@": '', ".com": '', "name position": '', \
    "email_position": ''}
  pos_at = 0
  pos_dotcom = 0
  answer = True
  for i in range(len(txt)):
    if txt[i] == "@":
      pos_at = i
      passed["@"] = "Passed"
      print("Passed:  @")
  for i in range(len(txt) - 3):
    if txt[i] == '.' and txt[i : i+ 4] == '.com':
      pos_dotcom = i
      passed[".com"] = 'Passed'
      print("Passed:  .com")
  if pos_at < pos_dotcom and (pos_dotcom -  pos_at) > 1:
    passed["email_position"] = "Passed"
    print('Passed: gmail.com')
  if pos_at != 0 and pos_dotcom != 0:
    print(txt[:pos_at])
    passed["name position"] = 'Passed'
    print("Passed:  name")
  print(passed)
  for item in passed:
    if passed[item] == '':
      answer = False
  return(answer)

