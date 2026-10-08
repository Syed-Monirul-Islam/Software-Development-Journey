s= input()

ans=[]
temp =""
count_L =0
count_R = 0

for ch in s:
    temp += ch
    if ch == 'L':
        count_L +=1
    elif ch == 'R':
        count_R +=1

    if count_L == count_R:
        ans.append(temp)

        temp =""
        count_L =0
        count_R =0
print(len(ans))

for item in ans:
    print(item)