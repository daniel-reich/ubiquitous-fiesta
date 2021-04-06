
def security(txt):
    txt = txt.replace("x", "")
    return ["Safe", "ALARM!"]["T$" in txt or "$T" in txt]

