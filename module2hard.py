n = int(input("Введите число из левой вставки:"))
chisla1 = []
chisla2 = []
for z in range(n):
    chisla1.append(z+1)
    chisla2.append(z+1)
answer = []
for i in range(n):
    x=chisla1[i]
    for k in range(n):
        y = chisla2[k]
        sum = x+y
        if n % sum ==0 and x < y:
            answer.append([x,y])
answer_1 = []
for g in range(len(answer)):

    answer_1.extend(answer[g])
print(*answer_1)

