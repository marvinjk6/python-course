
def is_prime(number):
  if number <= 1:
    return False
  for i in range(2, number): # vai checar do dois até o último numero antes do próprio número
    if number % i == 0:
      return False
  return True

print(is_prime(11))