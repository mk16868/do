# !/use/bin/python
# -*-coding:utf8-*-
###############################################################################99乘法表
for m in range(1,10):
    for n in range(1,10):
        if m>=n:
            print('%d×%d=%d'%(n,m,m*n),end='\t')
    print()

a = 0
while a<9:
    a +=1
    b = 0
    while b<9:
        b +=1
        if a>=b:
            print('%d×%d=%d'%(b,a,b*a),end='\t')
    print()
1
2
3
