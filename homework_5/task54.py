# Создать (программно) текстовый файл, записать в него
# программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


if __name__ == '__main__':

    f_obj = open("task54_file.txt", 'w')

    for i in range(1, 5):
        f_obj.write(str(i) + " \n")

    f_obj.close()

    f_obj = open("task54_file.txt", 'r')
    content = f_obj.readlines()
    f_obj.close()

    sum = 0
    for i in range(0, len(content)):
        sum = sum + int(content[i])

    print(sum)