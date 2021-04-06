
import re
​
whole = '\d+'
decimal = '\d*\.\d+'
either = '(?:{}|{})'.format(whole, decimal)
frame = '(?<= ){}(?= )'
​
integers = frame.format('[+-]?{}'.format(whole))
floats = frame.format('[+-]?{}'.format(decimal))
positive = frame.format('\+?{}'.format(either))
negative = frame.format('-{}'.format(either))
numbers = frame.format('[+-]?{}'.format(either))

