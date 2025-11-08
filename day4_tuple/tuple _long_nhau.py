students = (
    ("Alice", (9, 8, 10)),
    ("Bob", (7, 6, 9)),
    ("Anna", (10, 10, 9))
)

# a. In ra điểm trung bình của từng học sinh
for name, score in students:
    avg = sum(score) / len(score)
    print(f"{name}:{avg:.2f}")

# b. In ra tên học sinh có điểm trung bình cao nhất

best_name = None
best_avg = -1

for name, score in students:
    avg = sum(score) / len(score)
    if avg > best_avg:
        best_avg = avg
        best_name = name
print(f"Hoc sinh co diem trung binh cao nhat la: {best_name}:{best_avg:.2f}")