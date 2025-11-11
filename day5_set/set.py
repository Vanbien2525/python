# Set:
#     - không có thứ tự
#     - Không chứa phần tử trùng lập
#     - chứa các kiểu dữ liệu khác nhau (miễn chúng không thay đổi được)
#     - có thể thêm, xóa phần tử
#     - hỗ trợ các phép toán

thisset = {"apple", "banana", "chery"}
print(thisset)

thisset = set(("apple", "banana", "cherry"))
print(thisset)

print(type(thisset))

#get len()
print(len(thisset))
  
print("banana" in thisset) #not in

#add items
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#add set
thisset = {"apple", "banana", "cherry"}
tropical = {"orange", "kiwi", "mango"}
thisset.update(tropical)
print(thisset)

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

# my_set = {[1, 2], "hi"}  error because list
# print(my_set)

#remove Items
# remove()
thisset = {"apple", "banana", "cherry"}
thisset.remove("apple")     #note: neu xoa item khong co trong set thi se BI loi
print(thisset)

# discard()
thisset = {"apple", "banana", "cherry"}
thisset.discard("kiwi")     #note: neu xoa item khong co trong set thi KHONG Bi loi
print(thisset)

# pop()
thisset = {"apple", "banana", "cherry"}
thisset.pop()
print(thisset)      #note: pop() dung de xoa NGAU NHIEN item trong set

# clear()
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)      #note: clear() xoa cac item nhung van con set()

# del
thisset = {"apple", "banana", "cherry"}
del thisset         #note: del xoa luon set()

#loop set
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
  
#Join Sets
# union() va update(): ket hop tat ca item tu 2 set
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)     #same  set3 = set1 | set2  ( | chỉ cho phép bạn hợp nhất các tập hợp với các tập hợp khác, không phải với các kiểu dữ liệu khác)
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)        #same   myset = set1 | set2 | set3 |set4
print(myset)

# intersection(): sẽ trả về một tập hợp mới chỉ chứa các phần tử có mặt trong cả hai tập hợp.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)      #same: set3 = set1 & set2  (& chỉ cho phép bạn hợp nhất các tập hợp với các tập hợp khác, không phải với các kiểu dữ liệu khác)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)      #note: giong nhu intersection nhung thay vi return new set thi no thay doi set1
print(set1)

# difference() : trả về một tập hợp mới chỉ chứa các mục từ tập hợp đầu tiên mà không có trong tập hợp kia.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}     
set3 = set1.difference(set2)        #same: set3 = set1 - set2   (- chỉ cho phép bạn hợp nhất các tập hợp với các tập hợp khác, không phải với các kiểu dữ liệu khác)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)        #note: giong nhu difference nhung thay vi return new set thi no thay doi set1
print(set1)

# symmetric_difference() : trả về một tập hợp mới sẽ giữ lại chỉ các phần tử không có trong cả hai tập hợp.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)      #same: set3 = set1 ^ set2  (^ chỉ cho phép bạn hợp nhất các tập hợp với các tập hợp khác, không phải với các kiểu dữ liệu khác)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)      #note: giong nhu symmetric_difference nhung thay vi return new set thi no thay doi set1
print(set1)

#Python frozenset: Khác với tập hợp, các phần tử không thể thêm hoặc loại bỏ khỏi một frozenset.
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))