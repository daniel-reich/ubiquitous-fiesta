
import re
​
integers = '(?<=\s)[+-]?\d+(?=\s)'
floats = '(?<=\s)[+-]?(?:\d+)?\.\d+(?=\s)'
positive = '(?<=\s)\+?(?:\d+)?\.?\d+(?=\s)'
negative = '(?<=\s)-(?:\d+)?\.?\d+(?=\s)'
numbers = '(?<=\s)[+-]?(?:\d+)?\.?\d+(?=\s)'

