def cycle():
    try:
        number1 = float(input('Введите первое число:'))
        operation = input('Что сделать?: (+,-,/,*:)')
        result=0
        number2 = float(input('Введите второе число:\n'))

        if operation == "+":
            result = ("Результат:", number1 + number2)
        elif operation == '-':
            result = ("Результат:", number1 - number2)
        elif operation == '/':
            result = ("Результат:", number1 / number2)
        elif operation == '*':
            result = ("Результат:", number1 * number2)
        else:
            print('Ошибка')
            cycle()
            print(f"Результат: {result}")

    except (ValueError, ZeroDivisionError):


            print("Ошибка ввода")
            cycle()
# Для возможности продолжить работу программы, по своему выбору
            cycle()
while True:
    flag = input("Еще раз?[да/нет]")

    if flag == 'да':
            cycle()
    else:
        quit("конец")
