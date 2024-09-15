a = int(input("Введите число:"))
b = int(input("Введите число:"))
c = int(input("Введите число:"))
if a<(b+c) and b<(a+c) and c<(a+b):
    print("Треугольник существует")
else:
    print("Треугольник не существует")