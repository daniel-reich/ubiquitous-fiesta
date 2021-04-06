
import re
​
bounds = r'(?<=\s){}(?=\s)'
​
integersMatch = r'(?:\+|\-)?\d+'
integers = bounds.format(integersMatch)
​
floatsMatch = r'(?:\+|\-)?\d*\.\d+'
floats = bounds.format(floatsMatch)
​
positiveMatch = r'\+?\d*(?:\.\d+)?'
positive = bounds.format(positiveMatch)
​
negativeMatch = r'-\d*(?:\.\d+)?'
negative = bounds.format(negativeMatch)
​
numbersMatch = r'(?:{}|{}|{}|{})'.format(integersMatch, 
                                        floatsMatch, 
                                        positiveMatch, 
                                        negativeMatch)
numbers = bounds.format(numbersMatch)

