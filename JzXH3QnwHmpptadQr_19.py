
def bitwise_logical_negation(x):
  var = x
​
  var = (var >> 1) | var
  var = (var >> 1) | var
  var = (var >> 1) | var
  var = (var >> 1) | var
  var = (var >> 1) | var
  var = (var >> 1) | var
  var = (var >> 1) | var
  var = (var >> 1) | var
  var = (var >> 1) | var
  var = (var >> 1) | var
  var = (var >> 1) | var
  var = (var >> 1) | var
  var = (var >> 1) | var
  var = (var >> 1) | var
  var = (var >> 1) | var
  var = (var >> 1) | var
  var = (var >> 1) | var
  var = (var >> 1) | var
  var = (var >> 1) | var
  var = (var >> 1) | var
  var = (var >> 1) | var
  var = (var >> 1) | var
  var = (var >> 1) | var
​
  return (var & 1) ^ 1

