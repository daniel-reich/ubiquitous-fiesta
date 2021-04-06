
def security(s):
    s = s.replace("x", "")
    return ["Safe", "ALARM!"]["T$" in s or "$T" in s]

