# Tạo một movies list chứa tên các bộ phim đã xem
movies = ["yellow stone",
          "I love you",
          "Anh yeu em",
          "Gio",
          "One Piece",
          "Harry Potter",
          "Avengers",]
print(movies)
print()

# Sử dụng hàm input để nhập vào một bộ phim khác không có trong movies list
input_movies = input(f"Nhap ten film chua xem {movies}: ")
print(movies)
print()

# Thêm bộ phim vừa nhập vào cuối của danh sách movies
movies.append(input_movies)
from pprint import pprint
pprint(movies)
print()

# In ra bộ phim đầu tiên, cuối cùng và ở giữa movies list
print(f"phim dau tien: {movies[0]}")
print(f"phim cuoi cung: {movies[-1]}")
mid_movies = len(movies) // 2
print(f"phim o giua: {movies[mid_movies]}")
print()

# Tính tổng bộ phim có trong movies
movies_count = len(movies)
print(f"tong so phim co trong danh sach la: {movies_count}")
print()
# Xóa bộ phim đầu và cuối trong movies
movies.remove(movies[0])
movies.remove(movies[-1])
pprint(movies)
print()
# Lấy ra và xóa bộ phim cuối cùng trong movies
# Chèn một bộ phim bất kỳ vào đầu danh sách movies
# Đếm số bộ phim có tiêu đề là "One Piece"
# Tìm vị trí của bộ phim có tên là "gió"
# Thêm một danh sách bộ phim khác vào cuối danh sách movies ban đầu
# Xóa tất cả các bộ phim có trong danh sách