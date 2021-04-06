
def strip_url_params(url, params_to_strip=None):
  if params_to_strip == None:
    params_to_strip = []
  l = url[19:].split("&")[::-1]
  appeared = []
  answer = []
  if l[0] != "":
    for el in l:
      if appeared.count(el[0]) == 0 and params_to_strip.count(el[0])==0:
        appeared.append(el[0])
        answer.append(el)
    if len(answer) > 0:
      answer.sort()
      output = "https://edabit.com?" + answer[0]
      for el in answer[1:]:
        output += "&" + el
    else:
      output = "https://edabit.com"
    return output
  else:
    return "https://edabit.com"

