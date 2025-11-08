# QUẢN LÝ SẢN PHẨM (Nhập và lưu tuple)
# Yêu cầu: Nhập tên, giá, số lượng; lưu thành tuple; thêm vào list products; in danh sách.

products = []

name = input("Ten san pham: ")
price = float(input("Gia: "))
qty = int(input("So luong: "))

product = (name, price, qty)
products.append(product)

print("\nDanh sach san pham:")

for product in products:
    print(product)