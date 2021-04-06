
import re
def validate_relationships(txt):
    return eval(re.sub('(?<=\d)=(?=-?\d)','==', txt))

