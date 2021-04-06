
import itertools
import re
def clean_up(files, sort):
  return [list(group) for key, group in itertools.groupby(files, key = lambda x: re.findall(r'\w*(?=\.)', x))] if sort == 'prefix' else [list(group) for key, group in itertools.groupby(files, key = lambda x: re.findall(r'(?<=\.)\w*', x))]

