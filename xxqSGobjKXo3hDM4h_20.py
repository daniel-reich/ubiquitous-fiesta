
import re
def ing_extractor(string):
    ans = re.findall(r'\w*[aeiou\*]+\w*ing\b',string,re.I)
    return ans

