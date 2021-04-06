
def security(txt):
  if "T$" in txt.replace("x", "") or "$T" in txt.replace("x", ""):
    return "ALARM!"
  return "Safe"

