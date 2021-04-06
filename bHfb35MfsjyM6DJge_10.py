
def route_diff(directions):
  horiz_optim = abs(directions.count("E") - directions.count("W"));
  vert_optim  = abs(directions.count("N") - directions.count("S"));
  optimal_steps  =   horiz_optim  + vert_optim;
  return len(directions) - optimal_steps;

