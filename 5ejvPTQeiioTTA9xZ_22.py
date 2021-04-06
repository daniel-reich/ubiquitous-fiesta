
from typing import Any, Union
​
​
def get_type(var: Any) -> str:
  return type(var).__name__
​
​
def int_or_string(var: Union[int, str]) -> str:
  return get_type(var)

