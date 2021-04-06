
import re
​
integers = "(?<=\s)[+-]?\d+(?=\s)"
floats = "(?<=\s)[+-]?(?:\d+)?\.\d+(?=\s)"
positive = "(?<= )\+?(?:\d+|\d*\.\d+)(?= )"
negative = "(?<= )-(?:\d+|\d*\.\d+)(?= )"
numbers = "(?<= )[+-]?(?:\d+)?\.?\d+(?= )"

