#Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.


if __name__ == '__main__':

    f_obj = open("task52_file.txt", "r")

    content = f_obj.readlines()

    print(f'Количество строк:: {content} =  {len(content)}')
    counter = 0
    for i in range(0, len(content)):
        file_string = content[i]
        content_string = file_string.split()
        for j in range(0, len(content_string)):
            counter = counter + 1
        print(f'Количество слов в строке:: {file_string} = {counter}')
        counter = 0
    f_obj.close()