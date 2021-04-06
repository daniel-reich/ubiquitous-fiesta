
import re
​
body_insert = r'(?<=<body>\n)'
body_append = r'(?=\n</body>)'
body_rewrite = r'(?<=<body>\n)((?:.*\n)*.*)(?=\n</body>)'

