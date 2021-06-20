from store import Store
from product import Product

mascotin = Store("Mascotin")

pedigree = Product("Pedigree", 2000, "comida seca",234)
doko = Product("Doko", 800, "comida seca",212)
galleta = Product("Smile",300,"Snack",122)
master = Product("Mastercat",1200,"Snack",110)

mascotin.add_product(pedigree) 
mascotin.add_product(doko)
mascotin.add_product(galleta)
mascotin.add_product(master)

for indice in range(len(mascotin.products)):
    mascotin.products[indice].print_info()

mascotin.inflation(0.05)

for indice in range(len(mascotin.products)):
    mascotin.products[indice].print_info()

mascotin.set_clearance("Snack",0.02)

for indice in range(len(mascotin.products)):
    mascotin.products[indice].print_info()

mascotin.sell_product(110)

for indice in range(len(mascotin.products)):
    mascotin.products[indice].print_info()