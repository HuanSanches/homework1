First = int(input('Введите первое целое число: '))
Second = int(input('Введите второе целое число: '))
Third = int(input('Введите первое целое число: '))
if First == Second and First == Third:
    print ("3")
elif First == Second or First == Third or First == Third:
    print("2")
else:
    print("0")
