
print('輸入月份',end= '')
m=int(input())
while not (0<m<13): #月份條件
    print('輸入月份',end= '')#重新輸入月
    m=int(input())
    
print('輸入日期',end= '')
d=int(input())
while not (0<d<32): #日期條件
    print('輸入日期',end= '')#重新輸入日
    d=int(input())    
print('輸入任意數',end= '')
n=int(input())
 
#開始主題
f=(m+d*2+n*3)%10
if f==0:
    print('不吉')
elif f<=3:
    print('普通')
elif f<=8:
    print('吉')
else:
    print('大吉')
    
 



 
    
