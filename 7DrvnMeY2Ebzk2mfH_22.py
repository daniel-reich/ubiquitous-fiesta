
import re
​
body_insert = "(?<=<body>\n)()"
body_append = "()(?=\n</body>)"
body_rewrite = "(?<=\n)\s+<p>[\s\S]+</p>"

