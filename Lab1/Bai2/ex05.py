so_gio_lam = float(input("Nhập số giờ làm việc: "))
luong_gio = float(input("Nhập lương theo giờ tiêu chuẩn: "))
gio_tieu_chuan = 44
gio_vuot_chuan = max(0, so_gio_lam - gio_tieu_chuan)
thuc_linh = (gio_tieu_chuan * luong_gio) + (gio_vuot_chuan * luong_gio * 1.5)
print("Lương thực lĩnh là: ", thuc_linh)