
import re
def parse_code(name):
 fulllist= (re.findall(r"[A-Za-z1-9]+",name))
 dict={}
 dict.update(first_name=fulllist[0], last_name=fulllist[1],id=fulllist[2])
​
​
 return dict

