# calcula o juros rendidos + o montante inicial (principal)
def calculate_simple_interest(principal, duration, interest):
  # total = principal + (principal * interest * 0.01 * duration)
  i = interest / 100
  total_amount = principal + (principal * duration * i)
  return total_amount

print(calculate_simple_interest(10000, 5, 5))
