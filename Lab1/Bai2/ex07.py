print("Nhap cac dong van ban (nhap 'done' de ket thuc):")
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)
    #chuyen cac dong thanh chu in hoa
    print("\n Cac dong van ban da nhap sau khi chuyen thanh in Hoa la:")
    for line in lines:
        print(line.upper())