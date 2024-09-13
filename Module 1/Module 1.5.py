immutable_var = 1, 2, "a", "b", True
print(immutable_var)
#immutable_var[0]= 112
#print(immutable_var) - данная команда исполняться не будет ввиду неизмености значения переменных кортежа (tuple).

Mutable_list = [1, 2, "a", "b", True]
print(Mutable_list)
Mutable_list[0]= "Вода"
print(Mutable_list)
