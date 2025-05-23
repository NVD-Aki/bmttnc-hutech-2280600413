#tong tat ca so chan
def tinh_tong_so_chan(lst):
    tong = 0
    for num in lst:
        # kiem tra so chan
        if num % 2 == 0:
            tong += num
    return tong
input_list = input("Nhap danh sach so nguyen (cach nhau boi khoang trang): ")
numbers = list(map(int, input_list.split(',')))
#su dung ham va in ra ket qua
tong_chan = tinh_tong_so_chan(numbers)
print("Tong cac so chan trong danh sach la:", tong_chan)