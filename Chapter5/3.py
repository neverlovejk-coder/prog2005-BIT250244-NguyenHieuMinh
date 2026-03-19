import matplotlib.pyplot as plt
san_pham = ['san pham a', 'san pham b', 'san pham c', 'san pham d', 'san pham e']
gia = [30, 25, 15, 20, 10]
plt.pie(gia, labels=san_pham, autopct='%1.1f%%')
plt.title('doanh so')
plt.show()