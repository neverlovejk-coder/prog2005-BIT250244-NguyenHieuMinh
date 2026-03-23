ds = list(map(int, input("nhap cac chu so cach nhau bang dau cach: ").split()))
tong_chan = 0
print("cac so chan:")
for so in ds:
    if so % 2 == 0:
        print(so, end=" ")
        tong_chan += so
print("\ntong:", tong_chan)