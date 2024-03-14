def calculate_fuel(distance):
  # Type your code
  fuel_needed = distance * 10
  if fuel_needed < 100:
    return 100
  else:
    return fuel_needed