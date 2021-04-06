
import re
def valid_name(name):
  regex = r'^([A-Z]\.\s([A-Z]\.\s)?|[A-Z][a-z]+\s([A-Z]\.\s|[A-Z][a-z]+\s)?)([A-Z][a-z]+)$'
  return bool(re.match(regex, name))

