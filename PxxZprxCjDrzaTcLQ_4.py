
import re
vowel_links=lambda t:len(re.findall('[aeiou] [aeiou]',t))>0

