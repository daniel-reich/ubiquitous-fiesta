
from datetime import*
def get_day(d):m,d,y=map(int,d.split("/"));return date(y,m,d).strftime('%A')

