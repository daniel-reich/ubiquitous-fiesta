
def security(s):
    return "ALARM!" if any([a in s.replace('x', '') for a in ["T$", "$T"]])else "Safe"

