from SinhVien import SinhVien

class QuanLySinhVien:
    listSinhVien = []
    
    def generate_id(self):
        maxId = 1
        if len(self.listSinhVien) == 0:
            return maxId
        for sv in self.listSinhVien:
            if sv.id > maxId:
                maxId = sv.id
                maxId += 1
        return maxId
    def soLuongSinhVien(self):
        return self.listSinhVien.__len__()
    def nhapSinhVien(self):
        svId = self.generate_id()
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh sinh vien: ")
        major = input("Nhap nganh hoc sinh vien: ")
        diemTB = float(input("Nhap diem trung binh sinh vien: "))
        sv = SinhVien(svId, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)
    
    def updateSinhVien(self, id):
        sv : SinhVien = self.findById(id)
        if sv is None:
            if (sv != None):
                name = input("Nhap ten sinh vien: ")
                sex = input("Nhap gioi tinh sinh vien: ")
                major = input("Nhap nganh hoc sinh vien: ")
                diemTB = float(input("Nhap diem trung binh sinh vien: "))
                sv._name = name
                sv._sex = sex
                sv._major = major
                sv._diemTB = diemTB
                self.xepLoaiHocLuc(sv)
            else:   
                print("Sinh vien da co ID ={} khong ton tai. ", format(id))
                
    def sortById(self):
            self.listSinhVien.sort(key=lambda x: x._id,  reversed=False)
            
    def sortByName(self):    
            self.listSinhVien.sort(key=lambda x: x._name,  reversed=False)
            
    def sortByDiemTB(self): 
            self.listSinhVien.sort(key=lambda x: x._diemTB,  reversed=False)
        
    def findById(self, Id):
            searchResult = None
            if(self.soLuongSinhVien() > 0):
                for sv in self.listSinhVien:
                    if (sv._id == Id):
                        searchResult = sv
            return searchResult
        
    def deletetById(self, Id):
        isDeleted = False
        sv = self.findById(Id)
        if sv != None:
            self.listSinhVien.remove(sv)
            isDeleted = True
        return isDeleted
    
    def xepLoaiHocLuc(self, sv):
        if sv._diemTB >= 8:
            sv._hoc_luc = "Gioi"
        elif sv._diemTB >= 6.5:
            sv._hoc_luc = "Kha"
        elif sv._diemTB >= 5:
            sv._hoc_luc = "Trung binh"
        else:
            sv._hoc_luc = "Yeu"
            
    def showSinhVien(self , listSV):
        print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8} ".format("ID", "Name","Sex", "Major", "DiemTB", "HocLuc"))
        if (listSV.__len__() > 0):
            for sv in listSV:
                print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}".format(sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hoc_luc))
        print("\n")
        
    def getListSinhVien(self):
        return self.listSinhVien