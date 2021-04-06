
import re
def same_length(txt):
    return False if len(re.compile(r"1+").findall(txt)) != len(re.compile(r"0+").findall(txt)) else False not in [len(i[0]) == len(i[1]) for i in zip(re.compile(r"1+").findall(txt), re.compile(r"0+").findall(txt))]

