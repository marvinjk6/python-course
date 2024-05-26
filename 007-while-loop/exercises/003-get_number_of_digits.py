
# 1234 // 10 -> 1
# 123 // 10 -> 2
# 12 // 10 -> 3
# 1 // 10 -> 4
# 0 

def get_number_of_digits(number):
  if number == 0:
    return 1
  
  if number < 0:
    return -1
  
  number_of_digits = 0

  while number > 0:
    number //= 10
    number_of_digits += 1
    
  return number_of_digits

print(get_number_of_digits(123))  # Output: 3
print(get_number_of_digits(9087))  # Output: 4
print(get_number_of_digits(6))  # Output: 1
