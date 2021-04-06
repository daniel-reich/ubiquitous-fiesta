
import re
​
integers = r'(?<=\s)[+-]{,1}\d+(?=\s)'
floats = r'(?<=\s)[+-]{,1}\d*\.\d+(?=\s)'
positive = r'(?<=\s)\+{,1}\d*\.*\d+(?=\s)'
negative = r'(?<=\s)\-\d*\.*\d+(?=\s)'
numbers = r'(?<=\s)[+-]{,1}\d*\.*\d+(?=\s)'

