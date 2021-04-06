
import re
def evaluate_polynomial(poly, num):            
    def eval_expr(string):
        regex_map = [(r'^([0-9]*[.])?[0-9]+$', lambda x: x.group(0)),
                 (r'\([^()]+\)', lambda x: eval_expr(x.group(0)[1:-1])),
                 (r'(.+)\+(.+)', lambda x: str(float(eval_expr(x.group(1))) +float(eval_expr(x.group(2))))),
                 (r'(.+)\-(.+)', lambda x: str(float(eval_expr(x.group(1))) -float(eval_expr(x.group(2))))),
                 (r'(.+)\*(.+)', lambda x: str(float(eval_expr(x.group(1))) *float(eval_expr(x.group(2))))),
                 (r'(.+)\/(.+)', lambda x: str(float(eval_expr(x.group(1))) /float(eval_expr(x.group(2))))),
                 (r'(.+)\^(.+)', lambda x: str(float(eval_expr(x.group(1)))**float(eval_expr(x.group(2)))))]
        for op, fun in regex_map:
            string = re.sub(op, fun, string)
        return string
    poly = re.sub(r'(\d|x)([x(])', r'\1*\2' ,poly) #explicit products
    poly = poly.replace('x', str(num))
    try: return float(eval_expr(poly))
    except: return 'invalid'

