
import re
def ing_extractor(string):
    return re.findall(r"\S*(?:[aeiou]|\*)\w*ing", string, re.I)

