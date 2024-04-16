class Client:
    clients = {}
    def __init__(self, date_book, name, count, date_entry, day, budget):
        self.date_book = date_book
        self.name = name
        self.count = count
        self.date_entry = date_entry
        self.day = day
        self.budget = budget
        self.client_status = False

    def info(self, date_book, name, count, date_entry, day):
        print(f'{self.date_book} пришла заявка на бронирование от {self.name}. Клиент планирует заселиться {self.date_entry} в номер на {self.count} чел. на {self.day} дн.')


