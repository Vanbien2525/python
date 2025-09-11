#  Nhập vào số nguyên n. Hãy thực hiện các công việc sau:
# tăng n lên 10 đơn vị
# gấp 3 lần n
# giảm n đi 9 đơn vị
# Cuối cùng in ra n

n = int(input("Nhap n: "))
n += 10
n *= 3
n -= 9

# in N
print(n)

x = int(input("Nhập số x: "))

print("x > 10 ?", x > 10)
print("x == 0 ?", x == 0)
print("x <= 100 ?", x <= 100)

a = True
b = False
c = True

print("a and b =", a and b)
print("a or b =", a or b)
print("not c =", not c)
print("(a and c) or b =", (a and c) or b)
