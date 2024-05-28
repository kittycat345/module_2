n = int(input("Введите число из левой вставки:"))
chisla1 = []
chisla2 = []
for z in range(n):
    chisla1.append(n+1)
#x=1
for k in range(n-3):
    if k+1 <= n-1-k:
        couple.append([])
        couple[k].extend([k+1,n-1-k])
print(couple)
answer_couple = []
for sum in range(len(couple)):
    sum1 = couple[sum][0]+couple[sum][1]
    if n % sum1 == 0:
        answer_couple.append(couple[sum])
print(answer_couple)





