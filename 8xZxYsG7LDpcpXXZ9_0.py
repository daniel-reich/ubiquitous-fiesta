
import re
​
categories = ['[A-Z]', '[a-z]', '[0-9]', '[!-/:-@\[-_{-~]']
zero_occ = '|'.join('(?!.*{})'.format(i) for i in categories)
not_three = '|'.join('(?!(.*{}){{3}})'.format(i) for i in categories)
​
disallowed = '\S*\s'
short, long = '(?=\S{6,15}$)', '(?=\S{16,30}$)'
​
invalid = '(?={}|{})|(?!{}|{})'.format(zero_occ, disallowed, short, long)
weak = '(?!{})({}|{}({}))'.format(zero_occ, short, long, not_three)
strong = '(?!{}){}'.format(not_three, long)

