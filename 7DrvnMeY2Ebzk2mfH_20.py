
import re
​
body_insert = "(?<=<body>\n)"
body_append = "(?=\n</body>)"
body_rewrite = "{}(?:.|\n)+{}".format(body_insert,body_append)

