
in_alpha=lambda w:sum(1+'abcdefghijklmnopqrstuvwxyz'.find(x.lower())for x in w if x.isalpha())%2<1

