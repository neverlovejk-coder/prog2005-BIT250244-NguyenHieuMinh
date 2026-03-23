m = int(input("bao nhieu hang: "))
n = int(input("bao nhieu cot: "))
A = []
B = []
print("ma tran a:")
for i in range(m):
    hang = []
    for j in range(n):
        while True:
            x = input(f"A[{i}][{j}] = ")
            if x.strip() == "":
                print("loi khong de trong")
            else:
                hang.append(int(x))
                break
    A.append(hang)
print("ma tran b:")
for i in range(m):
    hang = []
    for j in range(n):
        while True:
            x = input(f"B[{i}][{j}] = ")
            if x.strip() == "":
                print("loi khong de trong")
            else:
                hang.append(int(x))
                break
    B.append(hang)
C = []
for i in range(m):
    hang = []
    for j in range(n):
        hang.append(A[i][j] + B[i][j])
    C.append(hang)
print("ket qua:")
for row in C:
    print(row)