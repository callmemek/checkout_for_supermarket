class ShoppingCart:
    def __init__(self):
        self.items = {}
        self.total = 0.0
        
    def add_item(self, item_name, quantity, price):
        if quantity <= 0:
            raise ValueError("adding 0? you can't do that, silly!")
        if price <= 0:
            raise ValueError("price can't be negative, be for real!")
        
        if item_name in self.items:
            self.items[item_name]['quantity'] += quantity
        else:
            self.items[item_name] = {'quantity': quantity, 'price': price}
        
        self.total += quantity * price
        
    def remove_item(self, item_name, quantity):
        if item_name not in self.items:
            raise  ValueError("this isn't even in your cart!")
        if quantity <= 0:
            raise ValueError("smh you can't remove nothing!")
        if quantity > self.items[item_name]['quantity']:
            raise ValueError ("trying to remove more than you have")
        
        self.items[item_name]['quantity'] -= quantity
        self.total -= quantity * self.items[item_name]['price']
        
        if self.items[item_name]['quantity'] == 0:
            del self.items[item_name]
        
    def checkout (self, payment):
        if payment < self.total:
            raise ValueError("hmm not enough money, try again!")
        if self.total == 0:
            raise ValueError("your cart is empty, you can't checkout!")
        
        change = payment - self.total
        self.items = {}
        self.total = 0.0
        return change
        
    