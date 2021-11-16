import random

def is_valid(strn, x_r):
    if strn.isdigit():
        if 0 < int(strn) < int(x_r):
            return True
        else:
            return False
    else:
        return False

def povtor():
    print("Ещё раз? (y/n)")
    while True:
        ans = input()
        if ans == "y":
            return True
        elif ans == "n":
            return False
        else:
            print("Введите в английской раскладке 'y' для продолжения или 'n' для окончания игры:")



a = True
print("Добро пожаловать в числовую угадайку!")
while a:
    
    
    print("Я загадаю число в диапазоне от 1 до указанного вами положительного числа больше 1.")
    print("Введите любое число больше 1:")
    while True:
        x_right = input()
        if x_right.isdigit():
            x_r = int(x_right)
            if x_r > 1:
                break
            else:
                print("Нужно выбрать любое число, больше единицы.")
        else:
            print("Всё-таки нужно ввести число больше единицы.")
            
    x = random.randint(1, x_r)
    popitki = 0
    
    while True:
        popitki += 1
        print("Попытка", popitki)
        print("Введите число от 1 до", x_r, "включительно:")
        num = input()
        
        if is_valid(num, x_r+1):
            
            n = int(num)
            if n < x :
                print("Ваше число меньше загаданного, попробуйте еще разок.")
                continue
            if n > x :
                print("Ваше число больше загаданного, попробуйте еще разок.")
                continue
            if n == x:
                print("Вы угадали, поздравляем!")
                print("Число попыток = ", popitki)
                popitki = 0
                a = povtor()
                break
        else:
            print("Это не похоже на целое число от 1 до", x_r)
            print("Попробуй ещё раз.")
        
print ("Спасибо, что играли в числовую угадайку. Еще увидимся...")