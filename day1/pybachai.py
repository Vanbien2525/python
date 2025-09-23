#giai phuong trinh bac 2 ax^2 + bx + c = 0
import math

a = float(input("Nhap a = "))
b = float(input("Nhap b = "))
c = float(input("Nhap c = "))

if a == 0:
    if b == 0:
        if c == 0:
            print("Pt vo so nghiem")
        else:
            print("Pt vo nghiem")
    else:
        x = -c / b
        print(f"Phuong trinh co nghiem x = {x:.2f}")
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Pt vo nghiem!")
    elif delta == 0:
        x = -b / (2*a) 
        print(f"Phuong trinh co nghiem kep x = {x:.2f}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("Phuong trinh co 2 nghiem phan biet:")
        print(f"x1 = {x1:.2f}")
        print(f"x2 = {x2:.2f}")
