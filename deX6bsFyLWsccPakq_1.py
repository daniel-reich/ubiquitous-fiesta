
import re
​
h = '[01]\d|2[0-3]'
ms = '[0-5]\d'
​
pattern = r'\b(?<!:)(?:{}):(?:{})(?::{})?(?!:)\b'.format(h, ms, ms)

