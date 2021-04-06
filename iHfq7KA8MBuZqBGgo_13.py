
import functools as ft
import operator  as op
def is_legitimate(lst):
  return 1 not in lst[0] + lst[-1] + \
         list(ft.reduce(op.concat, ([r[0], r[-1]] for r in lst[1:-1])))

