class Product:
    def __init__(self, name, price, category, sku):
        self.name = name
        self.price = price
        self.category = category
        self.sku = sku

    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price = self.price * (1 + percent_change)
        else:
            self.price = self.price * (1 - percent_change)
        return self

    def print_info (self):
        print(f"Product:{self.name} from category: {self.category} has a price of ${self.price}")

    def __repr__(self) -> str:
        return f'{self.name}, {self.price}, {self.category}'