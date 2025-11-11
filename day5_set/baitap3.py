text = "python is easy and python is fun to learn"
# Hãy viết chương trình:
# Tách các từ ra (dùng .split())
words = text.split()
print(words)

# Dùng set để tìm các từ khác nhau trong đoạn văn
unique_words = set(words)
print("Các từ khác nhau:", unique_words)

# In ra số lượng và danh sách các từ duy nhất
print("Số lượng:", len(unique_words))