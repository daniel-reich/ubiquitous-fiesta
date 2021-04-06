
can_give_blood=lambda d,r:d.strip('-')in'O'+r if'-'in d else'+'in r and d.strip('+')in'O'+r

