n = 4
print("hinh1:")
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(1, end=" ")
    print()
print("\nhinh2:")
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(j, end=" ")
    print()
print("\nhinh3:")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
print("\nhinh4:")
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
print("\nhinh5:")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print(j, end=" ")
        else:
            print("  ", end="")
    print()
print("\nhinh6:")
for i in range(1, n + 1):
    for j in range(1, n - i + 2):
        if i == 1 or j == 1 or j == n - i + 1:
            print(j, end=" ")
        else:
            print("  ", end="")
    print()
print("\nhinh7:")
for i in range(1, n + 1):
    print("  " * (n - i), end="")
    for j in range(1, i + 1):
        print(i, end="   ")
    print()
print("\nhinh8:")
for i in range(1, n + 1):
    print("  " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print(
print("\nhinh9:")
for i in range(1, n + 1):
    print("  " * (n - i), end="")
    for j in range(1, i + 1):
        if i == n:
            print(j, end=" ")
        elif j == 1 or j == i:
            print(j, end=" ")
        else:
            print("  ", end="")
    for j in range(i - 1, 0, -1):
        if i == n:
        elif j == 1: # Biên bên phải
            print(j, end=" ")
        else:
            print("  ", end="")
    print()