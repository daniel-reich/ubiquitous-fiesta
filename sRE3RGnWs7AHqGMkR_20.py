
import re
​
integers    = r'(?<=\s)([+-]?[1-9]\d*)(?=\s)'
floats      = r'(?<=\s)([+-]?(?:\d+)?\.\d+)(?=\s)'
positive    = r'(?<=\s)(\+?(?:\d+)?\.\d+|\+?[1-9]\d*)(?=\s)'
negative    = r'(?<=\s)(-(?:\d+)?\.\d+|-[1-9]\d*)(?=\s)'
numbers     = r'(?<=\s)([+-]?[1-9]\d*|[+-]?(?:\d+)?\.\d+)(?=\s)'

