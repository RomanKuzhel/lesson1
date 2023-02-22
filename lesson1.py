try:
    number1 = float(input('Введите первое число:'))
    operation=input('Что сделать?: (+,-,/,*:)\n')
    number2=float(input('Введите второе число:\n'))

    if operation=="+":
        print("Результат:",number1+number2)
    elif operation=='-':
        print("Результат:",number1 - number2)
    elif operation=='/':
        print("Результат:",number1 / number2)
    elif operation=='*':
        print("Результат:",number1 * number2)



    else:
        print('Ошибка')


except ValueError:
    quit("Ошибка ввода")
except ZeroDivisionError:
    quit("Ошибка")















