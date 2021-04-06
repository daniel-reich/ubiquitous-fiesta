
import re
syllabification = lambda word : ".".join(re.search(r"^" + r"([pbtdkgG?fvszSZxhcjmnrly][aAeiou][pbtdkgG?fvszSZxhcjmnrly]{0,2})" * sum(word.count(vowel) for vowel in ['a', 'A', 'e', 'i', 'o', 'u']) + r"$", word).groups())

