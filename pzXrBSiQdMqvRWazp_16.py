
def score_calculator(easy, med, hard):
    seasy = easy * 5
    smed = med * 10
    shard = hard * 20
    some = seasy + smed + shard
    if easy < 0 or med < 0 or hard < 0:
        return 'invalid'
    else:
        return some

