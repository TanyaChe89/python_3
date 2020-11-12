from sys import argv

script_name, first_param, second_param, third_param = argv

print("Имя скрипта: ", script_name)
print("Выработка в часах:: ", first_param)
print("ставка в час:: ", second_param)
print("премия:: ", third_param)

print((int(first_param)*int(second_param))+int(third_param))