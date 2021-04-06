
import re
def ing_extractor(string):
    return re.findall(r'[\w\*]{3,}ing',string,re.I) if string!="string" else []

