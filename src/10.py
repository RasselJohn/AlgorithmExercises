#   Написать программу, определяющую количество "счастливых" трамвайных билетов с номерами,
#   принадлежащими заданному интервалу номеров от N1 до N2 (N1<=N2). 
#   Граничные номера входят в интервал.
#   Номер трамвайного билета представляет собой шестизначное неотрицательное число, 
#   записываемое без подавления незначащих нулей.
#   Номер считается счастливым, если суммы первых трех и последних трех его цифр равны.
#   Билет с номером 000000 существует.


def sum_digits(number):
    return number // 100 + (number % 100 // 10) + (number % 100 % 10)


N1 = "041122"
N2 = "777777"
countHappyTickets = 0

# Словарь, где ключ - суммы цифр трёхзначного числа,
# значение словаря - список со всеми возможными трёхзначными числа 
# с указанной суммой цифр.
d = {i: [] for i in range(0, 28)}
for i in range(0, 1000):
    d[sum_digits(i)].append(i)

leftN1 = int(N1[:3])
leftN2 = int(N2[:3])
rightN1 = int(N1[3:])
rightN2 = int(N2[3:])

# Если первые тройки чисел совпадают 
# - отбираем значения между вторыми тройками чисел.
if leftN1 == leftN2:
    countHappyTickets = len(list(filter(lambda x: rightN1 <= x <= rightN2,
                                        d[sum_digits(leftN1)])))
else:
    countHappyTickets = len(list(filter(lambda x: rightN1 <= x,
                                        d[sum_digits(leftN1)]))) + len(list(
        filter(lambda x: x <= rightN2, d[sum_digits(leftN2)])))
leftN1 += 1
while (leftN1 < leftN2):
    countHappyTickets += len(d[sum_digits(leftN1)])
    leftN1 += 1

print(countHappyTickets)
