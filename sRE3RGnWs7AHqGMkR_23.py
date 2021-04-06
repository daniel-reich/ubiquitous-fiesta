
import re
​
integers = r'(?<= )[+-]?\d+(?= )'
floats = r'(?<= )[+-]?\d*\.\d+(?= )'
positive = r'(?<= )\+?(?:\d+|\d*\.\d+)(?= )'
negative = r'(?<= )-(?:\d+|\d*\.\d+)(?= )'
numbers = r'(?<= )[+-]?(?:\d+|\d*\.\d+)(?= )'

