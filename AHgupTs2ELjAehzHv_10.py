
import re
​
opening_tags = r"<\w+(?:\s*\w+=\".*\")*>"
closing_tags = r"</\w+>"
all_tags = r"(?:<\w+(?:\s*\w+=\".*\")*>.*</\w+>)|(?:<\w+(?:\s*\w+=\".*\")*>)|(?:</\w+>)"

