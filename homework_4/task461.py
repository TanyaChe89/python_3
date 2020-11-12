from sys import argv
from itertools import count

script_name, init_number = argv

print("Имя скрипта: ", script_name)
print("Input number:: ", init_number)

counter=0
for el in count(int(init_number)):
    if counter > 5:
        break
    else:
        counter = counter+1
        print(el)
