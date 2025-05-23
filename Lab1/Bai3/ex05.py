#đếm số lần xuất hiện của các phần tử trong danh sách
def dem_xuat_hien(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict

input_string = input("Nhập danh sách các từ (cách nhau bởi dấu phẩy): ")
words_list = input_string.split(',')

so_lan_xuat_hien = dem_xuat_hien(words_list)
print("Số lần xuất hiện của các từ trong danh sách là:", so_lan_xuat_hien)