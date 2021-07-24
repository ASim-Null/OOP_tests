class CashRegister:

    list = []

    def __init__(self):

        self.total_items = None # {'item': 'price'}
        self.total_price = 0
        self.discount = 0

    def add_item(self, new_item, price):
        self.total_items += 1
        self.total_price += price
        self.list.append(new_item)
        return new_item

    def remove_item(self, delete_item, price):
        self.total_items -= 1
        self.total_price -= price
        self.list.remove(delete_item)
        return self.total_items

    def apply_discount(self, discount):
        self.total_price -= discount
        return

    def get_total(self, item_price, total):
        for item in list(self.list):
            total += item_price
            self.total_price = total
            if self.discount == True:
                apply_discount()
        print(list(self.list), total)

    def show_items(self):
        self.total_items = list(self.total_items)
        print(list(self.list))
        print(self.total_price)

    def reset_register(self):
        self.total_items = None
        self.total_price = None
        self.discount = None
        print("Ready for new transaction")
