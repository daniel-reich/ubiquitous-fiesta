
import re
​
def syllabification(word):
    syllables = re.findall(r'([^Aaeiou]{1,2}[Aaeiou][^Aaeiou])|([Aaeiou][^Aaeiou])', word[::-1])
    return '.'.join(''.join(i) for i in syllables)[::-1]

