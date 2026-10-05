
# args
def all_sum(*numbers):
    print(numbers)
    sum =0
    for num in numbers:
        sum =sum + num
    return sum

total = all_sum(45, 46,10, 85, 12, 32, 75)
print('all sum: ',total)

def do_a_lot(*args):
    print(args)

do_a_lot(10, 20, 30, 40,50)