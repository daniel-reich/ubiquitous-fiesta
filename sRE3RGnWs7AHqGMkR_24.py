
import re
​
integers = r"(?<=\s)(?:\+|-)?\d+(?!\.)(?=\s)"
floats = r"(?<=\s)(?:\+|-)?\d*\.\d+(?=\s)"
positive = r"(?<=\s)\+?\d*\.*\d+(?=\s)"
negative = r"(?<=\s)-\d*\.*\d+(?=\s)"
numbers = r"(?<=\s)(?:\+|-)?\d*\.*\d+(?=\s)"

