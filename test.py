dict = {'Жиренкова Надежда Евдокимовна': {'book_data': '01.03.2020', 'num_people': '1', 'date_departure': '04.03.2020', 'budget': '4400'}, 'Мясников Виссарион Яковович': {'book_data': '01.03.2020', 'num_people': '1', 'date_departure': '02.03.2020', 'budget': '3500'}, 'Бузинская Альбина Кирилловна': {'book_data': '01.03.2020', 'num_people': '1', 'date_departure': '04.03.2020', 'budget': '2200'}, 'Канадов Самуил Севастьянович': {'book_data': '01.03.2020', 'num_people': '2', 'date_departure': '02.03.2020', 'budget': '6600'}, 'Грядкин Порфирий Кондратиевич': {'book_data': '01.03.2020', 'num_people': '4', 'date_departure': '05.03.2020', 'budget': '8100'}, 'Нефёдова Марфа Потаповна': {'book_data': '01.03.2020', 'num_people': '3', 'date_departure': '04.03.2020', 'budget': '2200'}}


def get_today_orders(self, day):
    today_orders = []
    for order in dict:
        order_day = int((dict[order]['book_data'].split('.'))[0])
        if order_day == day:
            print(day)
            today_orders.append(order)
    return today_orders

for day in range(1, 4):
    l =