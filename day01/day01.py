# import 
for x in range(100,1000):
    hight = x % 10
    midille = x // 10 % 10
    low = x // 100
    if (hight ** 3 + midille ** 3 + low ** 3) == x:
        print(x)