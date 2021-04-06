
import re
def syllabification(word):
    expr=r"([^aAeiou][aAeiou][^aAeiou]{0,2}(?=[^aAeiou]|$))"
    return ".".join(re.findall(expr,word))

