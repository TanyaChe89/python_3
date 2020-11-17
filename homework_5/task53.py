# Создать текстовый файл (не программно), построчно записать
# фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.()
# Пример файла:

# Иванов 23543.12
# Петров 13749.32

# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4

# Необходимо написать программу, открывающую файл на чтение
# и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок
# строк должен записываться в новый текстовый файл.


import codecs


def get_cyrillic(latin):
    latin_to_cyrillic = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    return latin_to_cyrillic.get(latin)


if __name__ == '__main__':

    f_obj = codecs.open("task53_file1.txt", "r", "utf_8_sig")

    content = f_obj.readlines()
    sum_of_salaries = 0.0
    for i in range(0, len(content)):
        person_info = content[i].split()
        sum_of_salaries = sum_of_salaries + float(person_info[1])
        if float(person_info[1]) < 20000.0:
            print(f'{person_info[0]} получает зп = {person_info[1]}')

    print(f'Средняя зп = {sum_of_salaries / len(content)}')

    f_obj.close()

    f_obj1 = codecs.open("task53_file2.txt", "r", "utf_8_sig")
    content = f_obj1.readlines()
    f_obj1.close()

    for i in range(0, len(content)):
        line = content[i].split(" — ")
        new_line = line[0] + " - " + line[1]
        file_name = f'task53_file_{i}.txt'
        f_obj = open(file_name, 'w')
        f_obj.write(new_line)

    f_obj.close()
