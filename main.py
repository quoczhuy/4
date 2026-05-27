branch_count = int(input("Nhập số lượng chi nhánh: "))
for branch in range(1, branch_count + 1):
    print(f"\nChi nhánh {branch}")
    for classroom in range(1, 3):
        while True:
            student_count = int(
                input(f"Nhập số học viên lớp {classroom}: ")
            )
            if student_count < 0:
                print("Số học viên không hợp lệ. Vui lòng nhập lại.")
                continue
            if student_count == 0:
                print("Lớp vắng toàn bộ. Bỏ qua kiểm tra trạng thái.")
                break
            if student_count >= 20:
                print(f"Chi nhánh {branch} - Lớp {classroom}: ""Lớp học ổn định")
            else:
                print(f"Chi nhánh {branch} - Lớp {classroom}: ""Lớp cần được nhắc nhở theo dõi")
            break