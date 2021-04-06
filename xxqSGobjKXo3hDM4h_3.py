
def ing_extractor(s):
    return [i for i in s.split() if i[-3::].lower() =="ing" and len(i) > 5 and "str" not in i]

