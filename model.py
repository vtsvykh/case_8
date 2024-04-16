from hotel import *
from room import *
from client import *


with open('fund.txt', 'r', encoding='utf-8') as room_base:
    for line in room_base.readlines():
        num, type, capacity, comfort = line.split()
        room_inst = {'type': type, 'comfort': comfort, 'capacity': capacity}
        Hotel.rooms[num] = room_inst

with open('booking.txt', 'r', encoding='utf-8') as book_base:
    for line in book_base.readlines():
        book_data, surname, name, patronymic, num_people, date_entry, num_day, budget = line.split()
        format_date_entry = date_entry.split('.')
        day = int(format_date_entry[0])
        month = int(format_date_entry[1])
        year = int(format_date_entry[2])
        date_departure = f'{day + int(num_day):02d}.{month:02d}.{year:02d}'
        book_inst = {'book_data': book_data, 'num_people': num_people, 'date_departure': date_departure, 'budget': budget}
        Hotel.clients[f'{surname} {name} {patronymic}'] = book_inst


for day in range(1, 3):
    print(f'{day:02d}.03.2022')


