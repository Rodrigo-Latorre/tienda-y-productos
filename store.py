from product import Product

class Store:
    def __init__(self, namestore):
        self.name = namestore
        self.products = []

    def add_product (self, new_product):
        self.products.append(new_product)

    def sell_product (self, sku):
        for idx in range(len(self.products)):
            if self.products[idx].sku == sku:
                self.products.pop(idx)

    def inflation(self, percent_increase):
        for indice in range(len(self.products)):
            self.products[indice] = self.products[indice].update_price(percent_increase,True)

    def set_clearance (self, category, percent_discount):
        for indice in range(len(self.products)):
            if self.products[indice].category == category:
                self.products[indice] = self.products[indice].update_price(percent_discount,False)
