
import re
def edabit_in_string(txt):
    return 'YES' if re.search('e.*d.*a.*b.*i.*t', txt) else 'NO'

