
import re
​
integers = '(?<= )[\+-]?\d+(?= )'
floats = '(?<= )[\+-]?\d*\.\d+(?= )'
positive = '(?<= )\+?\d*\.?\d+(?= )'
negative = '(?<= )-\d*\.*\d+(?= )'
numbers = '(?<= )[\+-]?\d*\.*\d+(?= )'

