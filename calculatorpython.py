import math

zxc = 0  
rez = 0  

while zxc != 11:
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Возведение в степень")
    print("6. Квадратный корень")
    print("7. Факториал")
    print("8. Синус")
    print("9. Косинус")
    print("10. Тангенс")
    print("11. Exit")  
    
    try:
        zxc = int(input("Введите номер операции: ")) 
        if zxc > 11:
            print("Ошибка: Введена неверная операция.")
            continue      
        elif zxc == 1:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
            rez = num1 + num2
            print(f"Результат: {rez}")
        elif zxc == 2:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
            rez = num1 - num2
            print(f"Результат: {rez}")
        elif zxc == 3:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
            rez = num1 * num2
            print(f"Результат: {rez}")
        elif zxc == 4:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
            if num2 == 0:
                print("Ошибка: деление на 0.")
            else:
                rez = num1 / num2
        elif zxc == 5:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
            rez = num1 ** num2
            print(f"Результат: {rez}")
        elif zxc == 6:
            num = float(input("Введите число: "))
            if num < 0:
                print("Квадратный корень отрицательного числа не может быть.")
            else:
                rez = math.sqrt(num)
                print(f"Результат: {rez}")
        elif zxc == 7:
            num = float(input("Введите число: "))
            if num < 0:
                print("Факториал отрицательного числа не может быть.")
            else:
                rez = math.factorial(int(num))
                print(f"Результат: {rez}")
        elif zxc == 8:
            num = float(input("Введите число: "))
            rez = math.sin(num)
            print(f"Результат: {rez}")
        elif zxc == 9:
            num = float(input("Введите число: "))
            rez = math.cos(num)
            print(f"Результат: {rez}")
        elif zxc == 10:
            num = float(input("Введите число: "))
            rez = math.tan(num)
            print(f"Результат: {rez}")
        elif zxc == 11:
            print("Выход из калькулятора.")
            break
    except ValueError:
        print("Ошибка: Неверная операция.")
