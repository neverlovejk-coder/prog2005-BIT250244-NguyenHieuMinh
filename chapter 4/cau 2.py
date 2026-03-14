def tinh_trung_binh(danh_sach_sv):
    if not danh_sach_sv:
        return 0
    tong_diem = sum(danh_sach_sv.values())
    return tong_diem / len(danh_sach_sv)

# Thử nghiệm
sinh_vien = {"An": 8.5, "Bình": 7.0, "Chi": 9.0}
print(f"Điểm trung bình: {tinh_trung_binh(sinh_vien):.2f}")