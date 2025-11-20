# 10. In các số nguyên tố từ 1 đến 50
for num in range(2, 51):
    snt = True
    for i in range(2, num):
        if num % i == 0:
            snt = False
            break
    if snt:
        print(num, "la so nguyen to")