from models.user import User
from models.hall import Hall
from models.ticket import Ticket
from services.storage import load_data, save_data


def get_valid_input(prompt: str, validator) -> str | None:
    while True:
        value = input(prompt).strip()
        if value.lower() == "exit":
            return None
        if validator(value):
            return value
        print("Неверный ввод. Попробуйте снова.\n")


def get_int_in_range(prompt: str, lo: int, hi: int) -> int | None:
    while True:
        raw = input(prompt).strip()
        if raw.lower() == "exit":
            return None
        if raw.isdigit():
            num = int(raw)
            if lo <= num <= hi:
                return num
        print(f"Введите число от {lo} до {hi} или 'exit'.\n")


def main() -> None:
    data = load_data()
    hall = Hall(hall_state=data["hall_state"])
    tickets = data["tickets"]

    print(
        "Добро пожаловать в систему бронирования билетов!\n"
        "(Введите 'exit' в любой момент, чтобы выйти)\n"
    )

    first_name = get_valid_input("Введите имя: ", User._validate_name)
    if first_name is None:
        return

    last_name = get_valid_input("Введите фамилию: ", User._validate_name)
    if last_name is None:
        return

    phone = get_valid_input("Введите телефон (+7XXX-XXX-XX-XX): ", User._validate_phone)
    if phone is None:
        return

    user = User(first_name, last_name, phone)

    while True:
        hall.display()

        row = get_int_in_range("Выберите ряд (1‑5): ", 1, hall.ROWS)
        if row is None:
            return

        seat = get_int_in_range("Выберите место (1‑10): ", 1, hall.SEATS_PER_ROW)
        if seat is None:
            return

        if hall.is_seat_available(row, seat):
            break
        print("Это место уже занято. Попробуйте другое.\n")

    confirm = input("Подтвердить покупку? (да/нет): ").strip().lower()
    if confirm != "да":
        print("Покупка отменена.")
        return

    hall.book_seat(row, seat)
    ticket = Ticket(user, row, seat)
    tickets.append(ticket.to_dict())
    save_data(tickets, hall.hall_state)

    print("\n Билет оформлен!")
    print(f"GUID:  {ticket.guid}")
    print(f"Ряд:   {ticket.row}")
    print(f"Место: {ticket.seat}")


if __name__ == "__main__":
    main()
