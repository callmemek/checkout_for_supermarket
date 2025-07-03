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