a = int(input("Введите число:"))
if a%2==0 and a>0:
    print("Положительное четное")
elif a%2==0 and a<0:
    print("Отрицательно четное")
elif a%2==1 and a<0:
    print("Отрицательно нечетное")
elif a%2==1 and a>0:
    print("Положительное нечетное")
else:
    print("Ноль")

