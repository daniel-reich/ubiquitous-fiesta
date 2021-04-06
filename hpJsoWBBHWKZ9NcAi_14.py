
import re
​
​
def bird_code(lst):
    result = []
    for bird in lst:
        birdlst = re.findall(r'[\w]{2,}', bird)
        if len(birdlst) == 1:
            birding = birdlst[0][:4]
            result.append(birding.upper())
        elif len(birdlst) == 2:
            birding = birdlst[0][0:2] + birdlst[1][0:2]
            result.append(birding.upper())
        elif len(birdlst) == 3:
            birding = birdlst[0][0] + birdlst[1][0] + birdlst[2][0:2]
            result.append(birding.upper())
        elif len(birdlst) == 4:
            birding = birdlst[0][0] + birdlst[1][0] + \
                birdlst[2][0] + birdlst[3][0]
            result.append(birding.upper())
​
    return result

