class Shop:
    shopping_mall ='Jamuna'
    def __init__(self,buyer):
        self.buyer = buyer
        self.cart =[]

    def add_to_cart(self,item):
        self.cart.append(item)

moni =Shop('Moni')
moni.add_to_cart('shoe')
moni.add_to_cart('phone')
print(moni.cart)

toni =Shop('Toni')
toni.add_to_cart('book')
toni.add_to_cart('watch')
print(toni.cart)