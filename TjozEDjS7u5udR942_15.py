
import re
sort_authors = lambda s: sorted(s, key=lambda x: re.findall(r'\b\w+\.?\Z', x.lower())[0])

