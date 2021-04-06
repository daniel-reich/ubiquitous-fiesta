
import re
def remove_virus(files):
    r = re.sub(r"\w*(?:(?<!not)(?<!anti)virus|malware)\.exe,?\s*", "",files).rstrip(", ")
    return r+" Empty" if r=="PC Files:" else r

