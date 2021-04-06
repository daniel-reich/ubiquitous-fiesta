
query = """
select count(Name)
from customers
where Bill > 10000
and Visits <15
"""

