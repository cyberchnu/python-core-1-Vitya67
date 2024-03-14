def sum_even_nums_in_range(start, stop):
  # Type your code
  if not isinstance(start, int) or not isinstance(stop, int) or start > stop:
    return None

  total = 0
  for number in range(start, stop + 1):
    if number % 2 == 0:
      total += number
  return total