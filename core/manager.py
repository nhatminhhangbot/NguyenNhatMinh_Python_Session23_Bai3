from datetime import datetime


def check_duplicate_id(flight_id, flight_list):
    """Hàm kiểm tra trùng mã chuyến bay (đã chuẩn hóa chuỗi)"""
    cleaned_id = flight_id.strip().upper()
    for flight in flight_list:
        if flight["flight_id"] == cleaned_id:
            return True
    return False


def add_new_flight(flight_list):
    print("\n----- TIẾP NHẬN CHUYẾN BAY MỚI -----")
    flight_id = input("Nhập mã chuyến bay: ").strip().upper()
    if check_duplicate_id(flight_id, flight_list):
        print(f"[LỖI] Mã chuyến bay {flight_id} đã tồn tại!")
        return

    try:
        passengers = int(input("Nhập số lượng hành khách: "))
        if passengers < 0:
            print("[LỖI] Số lượng hành khách không thể là số âm!")
            return
    except ValueError:
        print("[LỖI] Số lượng hành khách phải là một số nguyên!")
        return

    depart_time_str = input(
        "Nhập thời gian cất cánh (YYYY-MM-DD HH:MM:SS): ").strip()
    try:
        datetime.strptime(depart_time_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        print(
            "[LỖI] Sai định dạng thời gian! Vui lòng nhập đúng chuẩn YYYY-MM-DD HH:MM:SS")
        return

    try:
        duration_min = int(input("Nhập số phút bay: "))
        if duration_min <= 0:
            print("[LỖI] Thời gian bay phải lớn hơn 0 phút!")
            return
    except ValueError:
        print("[LỖI] Số phút bay phải là một số nguyên!")
        return

    new_flight = {
        "flight_id": flight_id,
        "passengers": passengers,
        "depart_time": depart_time_str,
        "duration_min": duration_min
    }
    flight_list.append(new_flight)
    print(f">> Thêm chuyến bay {flight_id} thành công!")
