a = int(input("Введите номер дня недели:"))
if 0<a<6:
    print("Будни")
elif 5<a<8:
    print("Выходные")
else:
    print("Ошибка")