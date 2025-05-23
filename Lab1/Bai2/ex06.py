input_str = input("Nhập X, Y :")
dimension = [int(x) for x in input_str.split(",")]
rowNum = dimension[0]
colum = dimension[1]
muliplist= [[0 for col in range(colum)] for row in range(rowNum)]
for row in range(rowNum):
    for col in range(colum):
        muliplist[row][col] = row*col
print(muliplist)