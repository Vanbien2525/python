numbers = (5, 10, 15, 20, 25)
# a. Tính tổng của các phần tử
i = 0
total1 = 0
while i < len(numbers):
    total1 += numbers[i]
    i += 1
print("Tong la: ", total1)

#C2:
total2 = sum(numbers)
print("Tong la: ", total2)

# b. Tính giá trị trung bình
avg = total2 /len(numbers)
print("Gia tri trung binh la: ",avg)

# c. In ra phần tử lớn nhất và nhỏ nhất
largest = max(numbers)
print("Phan tu lon nhat la: ", largest)

smallest = min(numbers)
print("Phan tu nho nhat la: ", smallest)