
import itertools
lucky_seven=lambda l:any(sum(i)==7for i in itertools.combinations(l,3))

