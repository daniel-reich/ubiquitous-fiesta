
from functools import wraps
​
def memoize(fn):
  calls = []
  values = []
  @wraps(fn)
  def memoized(*args, **kwargs):
    if (args, kwargs) not in calls:
      values.append(fn(*args, **kwargs))
      calls.append((args, kwargs))
    return values[calls.index((args, kwargs))]
  return memoized
​
@memoize
def determinant(A):
  dim = len(A)
  if any(len(row)!=dim for row in A):
    raise TypeError("Not a square matrix")
  if dim==1:
    return A[0][0]
  det = 0
  for col in range(dim):
    det += (
      (1 if col%2==0 else -1)
      * A[0][col]
      * determinant([[row[i] for i in range(dim) if i!=col] for row in A[1:]])
    )
  return det

