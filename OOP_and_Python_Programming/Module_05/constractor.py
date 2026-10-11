class Phone:

    def __init__(self,owner,brand,price):
        self.owner =owner
        self.brand =brand
        self.price =price


my_phone = Phone('Moni','realme',24500)
print(my_phone.owner,my_phone.brand,my_phone.price)

father_phone =Phone('Father','Nokia',2200)
print(father_phone.owner,father_phone.brand,father_phone.price)
        