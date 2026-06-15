from datetime import datetime, timedelta


def calculate_eta(flight_list):
    print("\n----- TÍNH TOÁN THỜI GIAN HẠ CÁNH (ETA) -----")
    search_id = input("Nhập mã chuyến bay cần tính: ").strip().upper()

    found_flight = None
    for flight in flight_list:
        if flight["flight_id"] == search_id:
            found_flight = flight
            break

    if not found_flight:
        print(f"[LỖI] Không tìm thấy chuyến bay có mã {search_id}!")
        return

    dep_time = datetime.strptime(
        found_flight["depart_time"], "%Y-%m-%d %H:%M:%S")
    eta = dep_time + timedelta(minutes=found_flight['duration_min'])

    print(
        f"-> Chuyến bay {search_id} cất cánh lúc: {found_flight['depart_time']}")
    print(
        f"-> Thời gian hạ cánh dự kiến (ETA): {eta.strftime('%Y-%m-%d %H:%M:%S')}")
