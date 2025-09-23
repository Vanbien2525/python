#giai phuong trinh bac nhat

a = int(input("Nhap a = "))
b = int(input("Nhap b = "))
if(a == 0):
    if(b == 0):
        print("Phuong trinh vo so nghiem!")
    else:
        print("Phuong trinh vo nhgiem!")
else:
    x = float(-b/a)
    print(f"Phuong trinh co nghiem x = {x:.2f}")
