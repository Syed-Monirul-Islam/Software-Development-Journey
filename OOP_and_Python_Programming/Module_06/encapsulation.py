# encapsulation --> hide details
# access modifier: public,protected,private

class Bank :
    def __init__(self, holder_name,initial_deposit):
        self.holder_name = holder_name
        self._branch = 'banani 11'
        self.__balnce = initial_deposit

    def deposit(self,amount):
        self.__balnce += amount

    def get_balnce(self):
        return self.__balnce

    def withdraw(self,amount):
        if amount < self.__balnce:
            self.__balnce = self.__balnce - amount
            return amount

        else:
            return 'taka nai'
        
        
moni = Bank('Moni',10000)
print(moni.holder_name)
moni.deposit(40000)
print(moni.get_balnce())