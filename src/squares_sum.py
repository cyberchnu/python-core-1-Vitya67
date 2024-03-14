def squares_sum(n):
  # Type your code
  if not isinstance(n, int) or n < 1:
    return None

  total = 0
  for number in range(1, n + 1):
    total += number ** 2
  return total
