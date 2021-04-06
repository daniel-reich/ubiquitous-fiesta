
import re
​
opening_tags = r'<[^/].*?>'
closing_tags = r'</.*?>'
all_tags = r'<\w*\b[^>]*>.*</\w*>|<[^/].*?>|</.*?>'

