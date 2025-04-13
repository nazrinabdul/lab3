n = int(input("Sətirlərin (n) sayını daxil et: "))
m = int(input("Sutunların (m) sayını daxil et: "))
A = []

print("Massivin elementlərini daxil et:")
for i in range(n):
    sətir = []
    for j in range(m):
        element = int(input(f"A[{i}][{j}] = "))
        sətir.append(element)
    A.append(sətir)

for i in range(0, n, 2):  
    hasil = 1
    for j in range(m):
        hasil *= A[i][j]
    print(f"A[{i}] sətrinin elementlərinin hasili: {hasil}")
