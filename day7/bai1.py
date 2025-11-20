# 1. In số 1 → 20, nhưng số 5 thì in thêm “(five)”
for number in range(1, 21):
    if number == 5:
      print(number, "five")
    else: print(number)
print()

# 2. In số chẵn từ 1 → 50
for i in range(1, 51):
    if i % 2 == 0:
        print(i)
print()

# 3. In số 1 → 30, số chia hết cho 3 thì in Fizz
for fizz in range(1, 30):
    if fizz % 3 == 0:
        print("fizz")
    else:
        print(fizz)
print()

# Nhập 5 số, đếm số lớn hơn 10
count = 0
for i in range(1, 6):
    n = int(input("Nhap so: "))
    if n > 10:
        count += 1
print(f"co {count} so lon hon 10")