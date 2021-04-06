
import re
deep_sum=lambda l:sum(map(int,re.findall('[+-]*\d+',str(l))))

