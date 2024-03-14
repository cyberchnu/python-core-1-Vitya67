def mean(number):
  # Type your code
  if not isinstance(number, int) or number < 0:
    return None

  total = 0
  digits = 0
  while number > 0:
    digit = number % 10
    total += digit
    digits += 1
    number //= 10
  return total // digits
