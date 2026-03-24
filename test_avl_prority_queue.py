import unittest
from lab4additional import TicketSystem


class TestTicketSystem(unittest.TestCase):

    def setUp(self):
        self.system = TicketSystem()

    def test_show_tickets(self):
        print("\nТЕСТ: Вивід квитків")

        self.system.add_ticket("1", 100, "Regular")
        self.system.add_ticket("2", 200, "VIP")

        tickets = self.system.show_tickets()

        print("Список квитків:")
        for t in tickets:
            print(t)

        self.assertEqual(len(tickets), 2)

    def test_manual_input(self):
        system = TicketSystem()

        print("\n Тест системи бронювання")

        while True:
            print("\n1. Додати квиток")
            print("2. Забронювати квиток")
            print("3. Показати всі квитки")
            print("4. Вийти")

            choice = input("Вибери дію: ")

            if choice == "1":
                ticket_id = input("Введи ID: ")
                price = int(input("Введи ціну: "))
                ticket_type = input("Тип (VIP/Regular): ")

                system.add_ticket(ticket_id, price, ticket_type)
                print("Квиток додано")

            elif choice == "2":
                result = system.book_ticket()
                print(result)

            elif choice == "3":
                tickets = system.show_tickets()

                if not tickets:
                    print("Немає квитків")
                else:
                    print("\nСписок квитків:")
                    for t in tickets:
                        print(t)

            elif choice == "4":
                print("Вихід...")
                break

            else:
                print("Невірний вибір")

        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
