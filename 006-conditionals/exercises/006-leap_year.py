
def is_leap_year(year):

  if year <= 0:
    return False
  
  # não é divisível por 4
  if not year % 4 == 0:
    return False

  # é divisível por 4 mas não é divisível por 100
  if not year % 100 == 0:
    return True
  
  # div 4, div 100, div por 400
  if year % 400 == 0:
    return True
  
  # div 4, div 100, não é div por 400
  return False

print(is_leap_year(1900))
print(is_leap_year(2048))