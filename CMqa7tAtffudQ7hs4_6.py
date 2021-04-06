
def sorting_steps(l):
  isorted = sorted(enumerate(l), key=lambda i_v: i_v[1])
  todo = {a: b for b, (a, v) in enumerate(isorted)}
  steps = []
​
  while todo:
    a, b = next(iter(todo.items()))
    steps.append((a, b))
    todo = {{b: a}.get(i, i): todo[i] for i in todo if i != a}
​
  return steps

