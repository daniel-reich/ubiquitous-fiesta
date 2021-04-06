
def c_cipher(msg, keyword):
  if " " in msg:
    msg = "".join([x.lower() for x in msg if x.isalnum()])
    if not (len(msg) % len(keyword)) == 0: msg += "x" * (len(keyword) - (len(msg) % len(keyword)))
    result = ["" for x in range(len(keyword))]
    for i in range(len(msg)): result[i % len(keyword)] += msg[i]
    keyword2 = sorted(keyword)
    final = ""
    for i in keyword2: final += result[keyword.find(i)]
    return final
  keyword2 = sorted(keyword)
  result = [msg[x:x+int(len(msg) / len(keyword))] for x in range(0, len(msg), int(len(msg) / len(keyword)))]
  result2 = [result[keyword2.index(x)] for x in keyword]
  final = ""
  for i in range(len(result2[0])):
    for j in result2: final += j[i]
  return final

