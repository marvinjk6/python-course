
def next_fibonacci(threshold):
  a, b = 0, 1
  sum = 0

  while True:
    sum = a + b
    print(f"a={a} b={b} sum={sum}")
    if(sum > threshold):
      break
    a = b
    b = sum
    
  return sum

print("Resultado = ", next_fibonacci(20))