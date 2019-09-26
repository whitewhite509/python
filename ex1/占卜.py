
print('輸入月份')
m=int(input())
print('輸入日期')
d=int(input())
print('輸入任意數')
n=int(input())

f=(m+d*2+n*3)%10

if f==0:
    print('不吉')
elif f<=3:
    print('普通')
elif f<=8:
    print('吉')
else:
    print('大吉')
    
