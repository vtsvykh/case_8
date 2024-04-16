class Hotel:
    rooms = {}
    clients = {}

    def __init__(self):
        self.type_room = []

    @classmethod
    def get_today_orders(cls, day):
        today_orders = []
        for order in cls.clients:
            order_day = int((cls.clients[order]['book_data'].split('.'))[0])
            if order_day == day:
                today_orders.append(order)
        return today_orders

    def find_available_room(self, order, discount):


