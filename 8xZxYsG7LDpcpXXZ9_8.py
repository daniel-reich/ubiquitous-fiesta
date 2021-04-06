
import re
​
low = "a-z"
high = "A-Z"
num = "\d"
sym = """!"#$%&'\(\)\*+,-\./:;<=>?@\[\]^_\\\{\|\}\b"""
types = [low,high,num,sym]
all = "".join(types)
all_but_1 = ["".join(types[j] for j in range(4) if j!=i) for i in range(4)]
​
invalid = ".{,5}$|.{31,}|" + ".*[^{}].*|[{}]*$|[{}]*$|[{}]*$|[{}]*$".format(all, *all_but_1)
​
val = "".join("(?=[{1}]*[{0}][{1}]*$)".format(types[i], all) for i in range(4))
​
reps = "|".join("(?=[{1}]*[{0}][{1}]*[{0}]?[{1}]*$)".format(types[i], all_but_1[i])
                for i in range(4))
​
weak = "(?=.{6,30}$)"+"(?={})".format(val) + "(?=.{6,15}$|" + "(?:{}))".format(reps)
​
rreps = "".join("(?=[{1}]*(?:[{0}][{1}]*)".format(types[i], all) + "{3}$)"
                for i in range(4))
​
strong = "(?=.{16,30}$)" + rreps

