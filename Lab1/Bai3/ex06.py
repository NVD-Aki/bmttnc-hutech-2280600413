def xoa_phan_tu(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True  # Trả về True nếu xóa thành công
    else:
        return False

# Sử dụng
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print("Dictionary trước khi xóa:", my_dict)
key_to_delete = 'b'
result = xoa_phan_tu(my_dict, key_to_delete)   
if result:
    print("Phần tử đã được xóa từ Dictionary:", my_dict)
else:
    print("Phần tử không tồn tại trong Dictionary.")
