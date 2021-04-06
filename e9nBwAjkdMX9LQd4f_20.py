
import re
txt = "Hey...I'm a sad anime teen...and I use a ton of pauses and elipses....."
pattern = "\.{3,}"
re.findall(pattern, txt)

