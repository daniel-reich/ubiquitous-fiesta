
import re
construct_fence = lambda b: 'H'*int(1e6/int(re.sub(r'[$,]', '', b)))

