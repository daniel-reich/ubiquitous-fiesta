
import re
​
def edabit_in_string(txt):
    match = re.search('e.*d.*a.*b.*i.*t', txt)
    return 'YES' if match else 'NO'

