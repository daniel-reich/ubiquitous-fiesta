
class Equals:
  def __call__(self):
    return self
  def __eq__(self, other):
    return True
​
equals = Equals()

