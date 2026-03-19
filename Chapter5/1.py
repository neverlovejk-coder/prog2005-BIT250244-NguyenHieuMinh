import matplotlib.pyplot as plt
categories = ['xuat sac, gioi, kha, trung binh, kem']
values = [6, 10, 12, 4, 1]
plt.bar(categories, values, color='skyblue')
plt.title('ket qua')
plt.xlabel('loai')
plt.ylabel('so luong')

plt.show()