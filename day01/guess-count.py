import random

conut = random.randint(1, 100)

# 一共猜了几次
conuter = 0

while True:
    conuter += 1
    anwser = int(input('请输入一个数字！'))
    if anwser < conut:
        print('小一点！')
    elif anwser > conut:
        print('大一点！')
    else: 
        print('你猜了 %.2f 次猜对了' % conuter)
        break

if conuter > 7:
    print('你是傻逼吗！')