
import re
​
body_insert = r'(?<=\<body>\n)\B'
body_append = r'\B(?=\n\</body>)'
body_rewrite = r'(?s)(?<=\<body>\n).*?(?=\n\</body>)'

