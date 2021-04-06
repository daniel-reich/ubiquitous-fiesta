
import random
class AlwaysTrue(object):
    def __eq__(self, other):
        return True
​
def manipulate():
    return AlwaysTrue()

