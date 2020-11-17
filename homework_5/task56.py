# Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.

# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки,
# в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами
# и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
# {“average_profit”: 2000}].

# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:

# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

# Подсказка: использовать менеджер контекста.

import codecs

if __name__ == '__main__':
    f_obj = codecs.open("task56_file.txt", "r", "utf_8_sig")
    content = f_obj.readlines()
    f_obj.close()
    my_positive_dict = {}
    my_negative_dict = {}
    sum_income = 0
    positive_counter = 0;
    for i in range(0, len(content)):
        firm_info = content[i].split()
        firm_income = int(firm_info[2]) - int(firm_info[3])
        if firm_income > 0:
            sum_income = sum_income + firm_income
            positive_counter = positive_counter + 1
            my_positive_dict[firm_info[0]] = firm_income
        else:
            my_negative_dict[firm_info[0]] = firm_income

    my_average_dict = {"average_profit": sum_income / positive_counter}
    my_list = [my_positive_dict, my_negative_dict, my_average_dict]
    f_obj = open("task56_file.json", 'w')
    f_obj.write(str(my_list))
    f_obj.close()
