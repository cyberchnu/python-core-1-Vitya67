def int_within_bounds(number, lower_bound, upper_bound):
  # Type your code
  if not isinstance(number, int):
    return False
  return lower_bound <= number < upper_bound
