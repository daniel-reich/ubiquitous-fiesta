
import re;
def math_expr(expr):
   return len(re.sub(r"\d\s*[%+-/*]\s*\d","",expr)) == 0;

