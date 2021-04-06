
import re
​
body_insert = "(?<=<body>\n)"
body_append = "(?=\n</body>)"
body_rewrite = "(?<=<body>\n)(.|\s)*(?=\n</body>)"

