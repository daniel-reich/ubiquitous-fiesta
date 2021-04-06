
import re
​
body_insert = '(?<=<body>\n)'
body_append = '(?=\n</body>)'
body_rewrite = '{}[\s\S]+{}'.format(body_insert, body_append)

