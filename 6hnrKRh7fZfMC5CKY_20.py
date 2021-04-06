
import textwrap
def look_and_say(n):
    if len(str(n))%2: return "invalid"
    a = textwrap.wrap(str(n), 2)
    return int("".join([int(i[0])*i[1] for i in a]))

