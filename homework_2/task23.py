# Пользователь вводит месяц в виде целого числа от1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.


if __name__ == '__main__':
    month_number = int(input("Введите месяц в виде целого числа от1 до 12: "))

    months_list = ['зима', 'весна', 'лето', 'осень']

    months_dict = {1: 'зима',
                   2: 'зима',
                   3: 'весна',
                   4: 'весна',
                   5: 'весна',
                   6: 'лето',
                   7: 'лето',
                   8: 'лето',
                   9: 'осень',
                   10: 'осень',
                   11: 'осень',
                   12: 'зима'}

    if month_number ==1 or month_number == 2 or month_number == 12:
        print(f'\n Месяц из list: {months_list[0]}')
        print(f'\n Месяц из dict: {months_dict.get(month_number)}')
    elif month_number == 3 or month_number == 4 or month_number == 5:
        print(f'\n Месяц из list: {months_list[1]}')
        print(f'\n Месяц из dict: {months_dict.get(month_number)}')
    elif month_number == 6 or month_number == 7 or month_number == 8:
        print(f'\n Месяц из list: {months_list[2]}')
        print(f'\n Месяц из dict: {months_dict.get(month_number)}')
    elif month_number == 9 or month_number == 10 or month_number == 11:
        print(f'\n Месяц из list: {months_list[3]}')
        print(f'\n Месяц из dict: {months_dict.get(month_number)}')
    else:
        print(f'\n Месяц не найден')
