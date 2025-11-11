# Cho hai tập hợp (set)
art_students = {"John", "Max", "Anna", "Bob", "Obito"}
math_students = {"Max", "Mery", "David", "Anna", "Naruto", "John"}

# Tìm những người bạn học cả vẽ lẫn toán
both = art_students.intersection(math_students)
print(both)

# Tìm những người bạn học vẽ nhưng không học toán
art_but_math = art_students.difference(math_students)
print(art_but_math)

# Tìm những người bạn học toán nhưng không học vẽ
math_but_art = math_students.difference(art_students)
print(math_but_art)

# Tìm những người bạn học vẽ hay toán không phải cả hai
art_or_math = art_students.symmetric_difference(math_students)
print(art_or_math)

# Tìm tất cả những người bạn
all_all = art_students.union(math_students)
print(all_all)
