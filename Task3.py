def is_prime(number):
    del_num = 2
    while del_num ** 2 < number and number % del_num != 0:
        del_num += 1
    return del_num ** 2 > number


while True:
    try:
        num = int(input('Введите число от 2 до 100 000: '))
        if 2 <= num <= 100000:
            if is_prime(num):
                print('Число простое.')
            else:
                print('Число составное.')
            break
        else:
            print('Некорректный ввод!')
    except ValueError:
        print('Некорректный ввод!')