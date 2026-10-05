balance = 5000

def buy_things(item,price):
    #local scope variable
    # you can use access global variable without using the global keyword
    # but,if you want to modify a global variable, you have to use the global keyword

    global balance
    print(f'previous blance value', balance)
    balance = balance - price

    print(f'balance after buying {item}',balance)

buy_things('sunglass',1000)
print('global blance after buy', balance)
