
import re
def bomb(txt):
    return "There is no bomb, relax." if re.search("bomb", txt.lower()) == None else "Duck!!!"

