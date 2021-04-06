
import re
def edabit_in_string(txt):
    return 'YES' if len(re.findall(r'.*e.*d.*a.*b.*i.*t.*',txt))!=0 else 'NO'

