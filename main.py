from bintrees import FastRBTree

class TaxPenaltyDatabase:
    def __init__(self):
        self.database = FastRBTree()

    def print_database(self):
        print("База даних:")
        for person_id, penalties in self.database.items():
            print(f"Код: {person_id}")
            for penalty in penalties:
                print(f"Штраф: {penalty}")

    def print_data_by_id(self, person_id):
        if person_id in self.database:
            print(f"Дані для коду {person_id}:")
            for penalty in self.database[person_id]:
                print(f"Штраф: {penalty}")
        else:
            print("Користувача з таким кодом не знайдено.")

    def print_data_by_penalty_type(self, penalty_type):
        found = False
        print(f"Дані для штрафу типу {penalty_type}:")
        for person_id, penalties in self.database.items():
            for penalty in penalties:
                if penalty['type'] == penalty_type:
                    found = True
                    print(f"Код: {person_id}, Штраф: {penalty}")
        if not found:
            print("Штрафів з таким типом не знайдено.")

    def print_data_by_city(self, city):
        found = False
        print(f"Дані для міста {city}:")
        for person_id, penalties in self.database.items():
            for penalty in penalties:
                if penalty['city'] == city:
                    found = True
                    print(f"Код: {person_id}, Штраф: {penalty}")
        if not found:
            print("Штрафів для цього міста не знайдено.")

    def add_person(self, person_id, name, city):
        self.database.setdefault(person_id, [])
        print(f"Користувач {name} з кодом {person_id} та містом {city} доданий до бази даних.")

    def add_penalty(self, person_id, penalty_type, amount, city):
        if person_id in self.database:
            self.database[person_id].append({'type': penalty_type, 'amount': amount, 'city': city})
            print(f"Штраф типу {penalty_type} на суму {amount} для користувача з кодом {person_id} у місті {city} доданий до бази даних.")
        else:
            print("Користувача з таким кодом не знайдено.")

    def remove_penalty(self, person_id, penalty):
        if person_id in self.database:
            if penalty in self.database[person_id]:
                self.database[person_id].remove(penalty)
                print(f"Штраф {penalty} видалений для користувача з кодом {person_id}.")
            else:
                print("Штраф не знайдено.")
        else:
            print("Користувача з таким кодом не знайдено.")

    def update_person_info(self, person_id, name=None, city=None):
        if person_id in self.database:
            if name:
                print(f"Ім'я користувача з кодом {person_id} оновлено на {name}.")
            if city:
                print(f"Місто користувача з кодом {person_id} оновлено на {city}.")
        else:
            print("Користувача з таким кодом не знайдено.")

    def update_penalty_info(self, person_id, penalty, penalty_type=None, amount=None, city=None):
        if person_id in self.database:
            if penalty in self.database[person_id]:
                if penalty_type:
                    penalty['type'] = penalty_type
                if amount:
                    penalty['amount'] = amount
                if city:
                    penalty['city'] = city
                print(f"Інформацію про штраф {penalty} для користувача з кодом {person_id} оновлено.")
            else:
                print("Штраф не знайдено.")
        else:
            print("Користувача з таким кодом не знайдено.")

def main():
    database = TaxPenaltyDatabase()

    # Додавання персон та їх штрафів
    database.add_person(123456789, "Іванов Іван", "Київ")
    database.add_penalty(123456789, "Порушення ПДР", 500, "Київ")
    database.add_penalty(123456789, "Порушення ПДР", 300, "Київ")
    database.add_person(987654321, "Петров Петро", "Львів")
    database.add_penalty(987654321, "Порушення ПДР", 200, "Львів")

    # Вивід даних
    print("\n1. Повний друк бази даних:")
    database.print_database()

    print("\n2. Друк даних за конкретним кодом:")
    database.print_data_by_id(123456789)

    print("\n3. Друк даних за конкретним типом штрафу:")
    database.print_data_by_penalty_type("Порушення ПДР")

    print("\n4. Друк даних за конкретним містом:")
    database.print_data_by_city("Київ")

    # Додавання нових штрафів та оновлення інформації
    database.add_penalty(987654321, "Паркування на газоні", 100, "Львів")
    database.update_person_info(123456789, name="Іванов Петро", city="Одеса")
    database.update_penalty_info(987654321, {'type': "Паркування на газоні", 'amount': 100, 'city': "Львів"},
                                  penalty_type="Паркування на тротуарі", amount=150)

    # Видалення штрафу
    database.remove_penalty(987654321, {'type': "Порушення ПДР", 'amount': 200, 'city': "Львів"})

    # Вивід оновлених даних
    print("\n1. Оновлений повний друк бази даних:")
    database.print_database()

if __name__ == "__main__":
    main()
