
import re
​
pattern = r'/[a-z]{5}/[a-z]{4}.[pyw]{2,3}$'
​
bool(re.search(pattern, '/users/file.py'))

