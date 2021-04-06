
import re
def remove_virus(files):
    PC, *files = re.split(r': |, ', files)
    pattern = r'(?<!not)(?<!anti)(malware|virus)'
    files = filter(lambda x: not re.findall(pattern, x), files)
    return '{}: {}'.format(PC, ', '.join(files) or 'Empty')

