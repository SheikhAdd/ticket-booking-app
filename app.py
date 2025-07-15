from models.user import User
from models.hall import Hall
from models.ticket import Ticket
from services.storage import load_data, save_data

def main():
    data = load_data()
    hall = Hall(hall_state=data["hall_state"])
    tickets = data["tickets"]

    print("Добро пожаловать в систему бронирования билетов!\n(Введите 'exit' в любой момент, чтобы выйти)\n")

    # reg
    first_name = input("Введите имя: ").strip()
    if first_name.lower() == "exit": return

    last_name = input("Введите фамилию: ").strip()
    if last_name.lower() == "exit": return

    phone = input("Введите телефон (+7XXX-XXX-XX-XX): ").strip()
    if phone.lower() == "exit": return

    user = User(first_name, last_name, phone)
    if not user.is_valid():
        print("Неверные данные. Попробуйте снова.")
        return

    # zal
    hall.display()

    try:
        row = int(input("Выберите ряд (1-5): "))
        if row == "exit": return

        seat = int(input("Выберите место (1-10): "))
        if seat == "exit": return
    except ValueError:
        print("Некорректный ввод.")
        return

    if not hall.is_seat_available(row, seat):
        print("Место занято или не существует.")
        return

    confirm = input("Подтвердить покупку? (да/нет): ").strip().lower()
    if confirm != "да":
        print("Покупка отменена.")
        return

    hall.book_seat(row, seat)
    ticket = Ticket(user, row, seat)
    tickets.append(ticket.to_dict())
    save_data(tickets, hall.hall_state)

    print("\nБилет оформлен!")
    print(f"GUID: {ticket.guid}")
    print(f"Ряд: {ticket.row}, Место: {ticket.seat}")

if __name__ == "__main__":
    main()
