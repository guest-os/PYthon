f = open('config.txt', 'w')
a = 4000
while a <= 5000:
    f.write('点击:850, 550\n输入:%s\n暂停:0.01秒\n' % a)
    a += 1
f.close()