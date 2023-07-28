# count = range(101, 0, -2)
sun = 0
for x in range(101, 0, -2):
    if x % 2 == 0:
        print('我是读书人')
    else:
        print('我是纯露') 
    sun += x

print(sun)