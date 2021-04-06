
import re
def even_or_odd(s):
    o,v= sum(list(map(int,re.findall(r'[02468]',s)))) , sum(list(map(int,re.findall(r'[^02468]',s))))
    return 'Even and Odd are the same' if o==v else 'Even is greater than Odd' if v<o else 'Odd is greater than Even'

