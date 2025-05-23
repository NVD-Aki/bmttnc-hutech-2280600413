from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while (1 == 1):
    print("Truong trinh quan ly sinh vien")
    print("******************************Mennu******************************")
    print("***  1. Nhap sinh vien                                        ***")
    print("***  2. Cap nhat sinh vien                                    ***")
    print("***  3. Xoa sinh vien                                         ***")
    print("***  4. Tim kiem sinh vien                                    ***")
    print("***  5. Sap xep sinh vien theo ID                             ***")
    print("***  6. Sap xep sinh vien theo chuyen nganh                   ***")
    print("***  7. Hien thi danh sach sinh vien                          ***")
    print("***  0. Thoat                                                 ***")
    print("*****************************************************************")  
        
    key = int(input("Nhap lua chon: "))
    if key == 1:
        print("Nhap sinh vien")
        qlsv.nhapSinhVien()
        print("Them  sinh vien thanh cong")
    elif key == 2:
        if (qlsv.soLuongSinhVien() > 0):
            print("Cap nhat sinh vien")
            print("Nhap ID sinh vien can cap nhat: ")
            ID = int(input())
            qlsv.updateSinhVien(ID)
        else:
            print("Danh sach sinh vien trong!")
            
    elif key == 3:
        if qlsv.soLuongSinhVien() > 0:
            print("\n3. Xoa sinh vien")
            print("Nhap ID sinh vien can xoa: ")
            ID = int(input())
            if qlsv.deletetById(ID):
                print("Xoa sinh vien co ID = ", ID, "thanh cong")
            else:
                print("Khong ton tai sinh vien co ID = ", ID)
        else:
            print("Danh sach sinh vien trong!")
            
    elif key == 4:
        
        if qlsv.soLuongSinhVien() > 0:
            print("\n4. Tim kiem sinh vien theo ten")
            print("Nhap ten sinh vien can tim kiem: ")
            name = input()
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
        else:
            print("Danh sach sinh vien trong!")

    elif key == 5:
        if qlsv.soLuongSinhVien() > 0:
            print("\n5. Sap xep sinh vien theo diem Trung Binh")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("Danh sach sinh vien trong!")
            
    elif key == 6:
        if qlsv.soLuongSinhVien() > 0:
            print("\n6. Sap xep sinh vien theo ten")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("Danh sach sinh vien trong!")
            
    elif key == 7:
        if qlsv.soLuongSinhVien() > 0:
            print("\n7. Hien thi danh sach sinh vien")
            qlsv.showSinhVien(qlsv.getListSinhVien()) 
        else:
            print("Danh sach sinh vien trong!")
            
    elif key == 0:
        print("Cam on ban da su dung chuong trinh! Thoat!")
        break
    else:
        print("Lua chon khong hop le! Vui long nhap lai!")
        print("Hay lua chon chuc nang tu 0 den 7 trogn Menu!")