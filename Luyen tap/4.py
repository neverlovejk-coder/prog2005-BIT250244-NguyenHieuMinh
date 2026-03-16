#4
s = input("Nhap chuoi: ")
hoa = thuong = so = dacbiet = khoangtrang = nguyenam = phuam = 0
for i in s:
    if i.isupper():
        hoa += 1
    elif i.islower():
        thuong += 1
    if i.isdigit():
        so += 1
    if i.isspace():
        khoangtrang += 1
    if not i.isalnum() and not i.isspace():
        dacbiet += 1
    if i.lower() in "aeiou":
        nguyenam += 1
    elif i.isalpha():
        phuam += 1
print("Chu cai in hoa:", hoa)
print("Chu cai in thuong:", thuong)
print("Chu so:", so)
print("Ky tu dac biet:", dacbiet)
print("Khoang trang:", khoangtrang)
print("Nguyen am:", nguyenam)
print("Phu am:", phuam)