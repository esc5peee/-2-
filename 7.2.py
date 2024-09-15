a = int(input("Введите координату х:"))
b = int(input("Введите координату у:"))
c = int(input("Введите координату х:"))
d = int(input("Введите координату у:"))
if (a>8 or a<1) or (b>8 or b<1) or (c>8 or c<1) or (d>8 or d<1):
    print("Ошибка")
elif (a+2==c and b+1==d) or (a-2==c and b+1==d) or (a+2==c and b-1==d) or (a-2==c and b-1==d) or (a+1==c and b+2==d) or (a-1==c and b+2==d) or (a+1==c and b-2==d) or (a-1==c and b-2==d):
    print("YES")
else:
    print("NO")
