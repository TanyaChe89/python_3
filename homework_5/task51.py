# Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.


if __name__ == '__main__':

    f_obj = open("task51_file.txt", 'w')

    while True:
        input_string = input("Введите: ")
        if input_string == "":
            f_obj.close()
            exit(0)
        else:
            f_obj.write(input_string+"\n")

