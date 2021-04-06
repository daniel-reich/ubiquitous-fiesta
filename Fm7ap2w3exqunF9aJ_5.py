
import re
def count_lone_ones(n):
    return len(re.findall(r'(?<!1)1(?!1)', str(n)))

