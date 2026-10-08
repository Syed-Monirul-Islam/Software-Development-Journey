n = int(input())
a = list(map(int, input().split()))

count = 0

while True:
    all_even = True
    for x in a:
        if x % 2 != 0: 
            all_even = False
            break

    if not all_even:
        break

    a = [x // 2 for x in a]
    count += 1

print(count)