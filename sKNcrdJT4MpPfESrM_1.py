
import re
def remove_virus(files):
  items = files.split(': ')[1].split(', ')
  valid = [item for item in items if \
            not re.match(r'^(?!anti)(?!not).*virus\.\w+',item) and 
            not re.match(r'.*malware\.\w+',item)]
  return "PC Files: " + (', '.join(valid) if valid else 'Empty')

