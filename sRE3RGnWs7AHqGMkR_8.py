
import re
​
integers = "(?<=[^\d.+-])[-+]?\d+(?!.[\d\s])(?=[,\s])"
floats = "(?<=[^-+\d.])[-+]?\d*\.\d+(?=[^.\d])"
positive = "(?<=[^-\d.])[+]?\d+\.?\d*(?=[^.\d])"
negative = "(?<=[^-+\d.])-\d*(?:\.\d+)?(?=[^-.\d])"
numbers = "{}|{}".format(positive,negative)

