
import re
body_insert = i = "(?<=<body>\n)"
body_append = a = "(?=\n</body>)"
body_rewrite = i + "[\s\S]+" + a

