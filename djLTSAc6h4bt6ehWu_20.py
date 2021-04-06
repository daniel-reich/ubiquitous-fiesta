
import re
​
def camelCasing(txt):
    string_split = re.split('_| ',txt)
    string_split[0] = string_split[0].lower()
​
    for word in range(1, len(string_split)):
        string_split[word] = string_split[word].capitalize()
    camelCase_string = "".join(string_split)
​
    return camelCase_string

