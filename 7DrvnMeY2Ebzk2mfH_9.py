
import re
​
body_insert = "(?<=<body>\n)"
body_append = "(?=\n</body>)"
body_rewrite = "\s\s\s\s<p>[\d\D]*</p>"

