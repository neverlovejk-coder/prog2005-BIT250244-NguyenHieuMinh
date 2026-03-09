for i in range(1,6):
    for j in range(1,i+1):
        print(j, end="")
    print()

n = 5
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    if i == 1:
        print("*")
    elif i == n:
        for j in range(n):
            print("*", end=" ")
        print()
    else:
        print("*" + " " * (2 * i - 3) + "*")