
import re
​
is_there_consecutive = lambda lst, n, times: n not in lst if times == 0 else bool(re.search(r"" + str(n) + "{" + str(times) + "}", "".join(str(n) for n in lst)))

