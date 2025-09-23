# nhap vao so nguyen n
# tinh tong tat ca cac so le chia het cho 5

# tinh tbc cua tat ca so le chia het cho 5

n = int(input("Nhap n: "))
sum = 0
count = 0
for i in range(1, n+1):
    if(i % 2 == 1 and i % 5 == 0):
        sum += i
        count +=1
print(sum)

tbc = sum / count
print(tbc)