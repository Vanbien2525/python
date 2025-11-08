friends = [("Bob", "Male"), ("Anna", "Female"), ("Max", "Male")]

# a. Cho biết chiều dài của friends
print(f"chieu dai cuar tuple:{friends} la: {len(friends)}")

# b. Lấy ra phần tử đầu, cuối và giữa và kiểm tra kiểu của chúng
first = friends[0]
print("Phần tử đầu tiên:", first)
print(type(first))

mid = friends[-1]
print(f"Phan tu cuoi cung la: ", mid)
print(type(mid))

last = friends[len(friends) // 2]
print(f"Phan tu ow giua la: ", last)
print(type(last))

# c. Nhập vào tên (name) và giới tính (gender) của một người bạn sau đó append vào friends tuple gồm hai giá trị (name, gender) 
my_name = input("Nhap ten cua ban: ")
gender = input("Nhap gioi tinh: ")
my_tuple = (my_name, gender)
friends.append(my_tuple)
print(friends)
