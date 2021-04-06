
import re
unique_styles=lambda a:len(set(re.findall('\w[- \w]+','%s'%a)))

