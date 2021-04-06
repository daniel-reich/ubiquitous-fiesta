
import re
def remove_virus(files):
    pattern = r',? \S*(?<!not)(?<!anti)virus\.exe ?|,? \S*malware\.exe ?'
    ans = re.sub(pattern,'',files)
    return ans if len(ans) > 10 else ans + ' Empty'

