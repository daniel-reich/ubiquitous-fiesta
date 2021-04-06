
import re
​
body_insert = "(?<=<body>\n)"
body_append = "(?=\n</body>)"
body_rewrite = r"(?<=<body>\n)(?:.*(?:\n|\r\n?).*)*(?=\n</body>)"

