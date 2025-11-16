from pprint import pprint

album_info = {
    "album_name": "The Dark Side of the Moon",
    "band": "Pink Floyd",
    "release_year": 1973,
    "track_list": [
        "Speak to Me",
        "Breathe",
        "On the Run",
        "Time",
        "The Great Gig in the Sky",
        "Money",
        "Us and Them",
        "Any Colour You Like",
        "Brain Damage",
        "Eclipse"
    ]
}
# Lấy ra giá trị của các key sau: album_name, release_year bằng hai cách
print(album_info["album_name"])
print(album_info.get("album_name"))

print(album_info["release_year"])
print(album_info.get("release_year"))

# Thay đổi giá trị của key: release_year từ 1973 thành 1971
album_info["release_year"] = 1971
pprint(album_info)

# Xóa phần tử với key là track_list
del album_info["track_list"]
pprint(album_info)

# Thêm một key mới là amount = 2000 bằng hai cách
album_info["amount"] = 2000
# album_info.update(amount = 2000)
pprint(album_info)

# Làm trống dict: album_info
album_info.clear()
pprint(album_info)