
import re
​
integers = r"(?<= )[+-]?\d+(?= )"
floats = r"(?<= )[+-]?\d*\.\d+(?= )"
positive = r"(?<= )\+?\d+(?:\.\d+)?(?= )"
negative = r"(?<= )-\d*(?:\.\d+)?(?= )"
numbers = r"(?<= )[+-]?\d*(?:\.\d+)?(?= )"

