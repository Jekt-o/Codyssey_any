import json
import os

DATA_FILE = "attendance.json"


def load_data():
    """저장된 출석 데이터를 불러온다."""
    if not os.path.exists(DATA_FILE):
        return {}

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return {}


def save_data(data):
    """출석 데이터를 파일에 저장한다."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def add_attendance(data):
    """날짜와 이름을 입력받아 출석을 추가한다."""
    date = input("날짜를 입력하세요 (예: 2025-05-20): ").strip()
    name = input("이름을 입력하세요: ").strip()

    if not date or not name:
        print("날짜와 이름은 비워둘 수 없습니다.\n")
        return

    if date not in data:
        data[date] = []

    data[date].append(name)
    save_data(data)
    print(f"[완료] {date}에 {name} 출석이 추가되었습니다.\n")


def show_all_attendance(data):
    """전체 출석 목록을 보여준다."""
    if not data:
        print("저장된 출석 기록이 없습니다.\n")
        return

    print("\n=== 전체 출석 목록 ===")
    for date in sorted(data.keys()):
        print(f"\n[{date}]")
        for i, name in enumerate(data[date], start=1):
            print(f"{i}. {name}")
    print()


def show_attendance_by_date(data):
    """특정 날짜의 출석 목록을 보여준다."""
    date = input("조회할 날짜를 입력하세요 (예: 2025-05-20): ").strip()

    if date not in data:
        print("해당 날짜의 출석 기록이 없습니다.\n")
        return

    print(f"\n=== {date} 출석 목록 ===")
    for i, name in enumerate(data[date], start=1):
        print(f"{i}. {name}")
    print()


def main():
    data = load_data()

    while True:
        print("==== 스터디 출석부 ====")
        print("1. 출석 추가")
        print("2. 전체 출석 목록 보기")
        print("3. 날짜별 출석 보기")
        print("4. 종료")

        choice = input("메뉴를 선택하세요: ").strip()
        print()

        if choice == "1":
            add_attendance(data)
        elif choice == "2":
            show_all_attendance(data)
        elif choice == "3":
            show_attendance_by_date(data)
        elif choice == "4":
            print("프로그램을 종료합니다.")
            break
        else:
            print("올바른 메뉴 번호를 입력하세요.\n")


if __name__ == "__main__":
    main()
