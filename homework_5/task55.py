# Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб)
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

import codecs

if __name__ == '__main__':
    f_obj = codecs.open("task55_file.txt", "r", "utf_8_sig")
    content = f_obj.readlines()
    f_obj.close()
    my_dict = {}
    for i in range(0, len(content)):
        subject_info = content[i].split()

        name = subject_info[0]
        lecture = subject_info[1]
        practice = subject_info[2]
        lab = subject_info[3]
        if lecture == '—':
            lecture = 0
        else:
            lecture = lecture.split("(л)")[0]

        if practice == '—':
            practice = 0
        else:
            practice = practice.split("(пр)")[0]

        if lab == '—':
            lab = 0
        else:
            lab = lab.split("(лаб)")[0]

        my_dict[name] = int(lecture) + int(practice) + int(lab)

    print(my_dict)
