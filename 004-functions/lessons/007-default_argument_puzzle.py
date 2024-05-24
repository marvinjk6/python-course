def greet_user(name="User"):
  print(f"Hello, {name}!")

# greet_user() # default User
# greet_user("Alice")
# greet_user('Alice')


def print_string(str="Hello World", no_of_times=5):
  for i in range(1,no_of_times+1):
    print(str)

# print_string()
# print_string(no_of_times=6) # se passar só 6 ele seria o primeiro argumento, será printado 6 cinco vezes
# print_string(7, 8) # printa o 7 oito vezes
# print_string(7.5, 8)
# print_string(7.5, "eight") # erro -> não é possível somar "eight" + 1 na função range
print_string(no_of_times=3, str="Ordem trocada") # é possivel alterar a ordem dos argumentos quando o default é passado