
import re
​
def fauna_number(txt):
    fauna = ["muggercrocodile", "one-hornedrhino",
             "python", "moth", "monitorlizard", "bengaltiger"]
    return [(name, number) for number, name in re.findall(r"(\d+)\s([a-z-]+)", txt) if name in fauna]

