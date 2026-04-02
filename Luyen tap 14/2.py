n = 4
print("hinh1:")
for i in range(n):
    print("* " * n)
print("\nhinh2:")
for i in range(1, n + 1):
    print("* " * i)
print("\nhinh3:")
for i in range(n, 0, -1):
    print("* " * i)
print("\nhinh3:")
for i in range(1, n + 1):
    print("  " * (n - i) + "* " * i)
print("\nhinh5:")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print("\nhinh6:")
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == 1 or i == n or j == 1 or j == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print("\nhinh7:")
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j == n or i == n or j == n - i + 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print("\nhinh8:")
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
print("\nhinh9:")
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print("*", end=" ")
        else:
            print("  ", end="")
    print()
print("\nhinh10:")
for i in range(n, 0, -1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print("*", end=" ")
        else:
            print("  ", end="")
    print()