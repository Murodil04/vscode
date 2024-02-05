# # print(''' "Nexia", "Tico", 'Damas' ko\'rganlar \n qilar havas''')

# # print(5**4)

# # print(22/4-22//4)

# # print('yuzi ', 125**2, 'perimetr ',125*4 )

# # print('gipotenuza',(6**2+7**2)**(1/2))

# # ism="Hello World"
# # print(ism)

# # xabar="men talabaman"
# # print(xabar)
# # xabar="men dasturchiman"
# # print(xabar)

# # radius=5
# # pi=3.14
# # aylana_yuzi=pi*radius**2
# # print("Radius",radius,"ga teng aylananing yuzi=",aylana_yuzi)

# #8
# # a=int(input("a="))
# # b=int(input("b="))
# # o=(a+b)/2
# # print(f"orta arifmetik={o}")

# #9
# # a=int(input("a="))
# # b=int(input("b="))
# # o=(a*b)**(1/2)
# # print(f"orta arifmetik={o}")

# #10
# # a=int(input("a="))
# # b=int(input("b="))
# # y=a+b
# # k=a*b
# # print(f"a**2;b=**2;yigindi{y}")

# #IF_1 AND_2 AND_3
# # son=int(input("son="))
# # if (son>0):
# #     son=son+1
# #     print(son)
# # elif (son<0):
# #     son=son-2
# #     print(son)
# # elif (son==0):
# #     son=son+10
# #     print(son)

# #IF_4
# # a=int(input("a="))
# # b=int(input("b="))
# # c=int(input("c="))
# # if(a>0 and b>0 and c>0):
# #     print(3)
# # elif (a>0 and b>0 and c<0) or (a>0 and b<0 and c>0) or (a<0 and b>0 and c>0):
# #     print(2)
# # elif (a>0 and b<0 and c<0) or (a<0 and b>0 and c<0) or (a<0 and b<0 and c>0):
# #     print(1)

# #IF_5
# # a=int(input("a="))
# # b=int(input("b="))
# # c=int(input("c="))
# # if(a>0 and b>0 and c>0):
# #     print('3 ta musbat')
# #     print('0 ta manfiy')
# # elif (a>0 and b>0 and c<0) or (a>0 and b<0 and c>0) or (a<0 and b>0 and c>0):
# #     print('2 ta musbat')
# #     print('1 ta manfiy')
# # elif (a>0 and b<0 and c<0) or (a<0 and b>0 and c<0) or (a<0 and b<0 and c>0):
# #     print('1 ta musbat')
# #     print('2 ta manfiy')
# # elif(a<0 and b<0 and c<0):
# #     print('0 ta musbat')
# #     print('3 ta manfiy')

# #IF_6
# # a=int(input("a="))
# # b=int(input("b="))
# # if (a>b):
# #     print('kattasi=>',a)
# # elif (b>a):
# #     print('kattasi=>',b)    

# #IF_7
# # a=int(input("a="))
# # b=int(input("b="))
# # if (a>b):
# #     print(2)
# # elif (b>a):
# #     print(1)    

# #IF_8
# # a=int(input("a="))
# # b=int(input("b="))
# # if (a>b):
# #     print('kattasi=>',a)
# #     print('kichkinasi=>',b)
# # elif (b>a):
# #     print('kattasi=>',b) 
# #     print('kichigi=>',a)   

# #IF_9
# # a=int(input("a="))
# # b=int(input("b="))
# # if (a>b):
# #     c=a
# #     a=b
# #     b=c
# #     print(a,b)
# # elif (b>a):
# #     print(a,b)   
 
# #IF_10
# # a=int(input("a="))
# # b=int(input("b="))
# # if (a!=b):
# #     print(a+b)
# # elif (a==b):
# #     print(0)

# # #IF_11
# # a=int(input("a="))
# # b=int(input("b="))
# # if (a>b):
# #     print(a+b)
# # if (b>a):
# #     print(b)    
# # elif (a==b):
# #     print(0)
# # #IF_12
# # a=int(input("a="))
# # b=int(input("b="))
# # c=int(input("c="))
# # if (a<b and b<c) or (a<c and c<b):
# #     print('kichigi=>a',a)
# # elif (b<c and c<a) or (b<a and a<c):
# #     print('kichigi=>b',b)
# # elif (c<b and b<a) or (c<a and a<b):
# #     print('kichigi=>',c)

# ##IF_13
# # a=int(input("a="))
# # b=int(input("b="))
# # c=int(input("c="))
# # if (a<b and b<c) or (c<b and b<a):
# #     print(b)
# # elif (b<c and c<a) or (a<c and c<b):
# #     print(c)
# # elif (c<a and a<b) or (b<a and a<c):
# #     print(a)

# #IF_14 
# # a=int(input("a="))
# # b=int(input("b="))
# # c=int(input("c="))
# # if (a<b and a<c and b<c):
# #     print(a ,c)
# # elif (b<c and b<a and c<a):
# #     print(b,  a)
# # elif (c<b and c<a and a<b) :
# #     print(c,b)

# ##IF_15
# # a=int(input("a="))
# # b=int(input("b="))
# # c=int(input("c="))
# # if (a<b and a<c):
# #     print(b+c)
# # elif (b<c and b<a):
# #     print(a+c)
# # elif (c<b and c<a) :
# #     print(b+a)

# #16
# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))
# if (a<b<c) :
#     print(2*a, 2*b, 2*c)
# else :
#     print(-1*a, -1*b, -1*c)

#17
# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))
# if (a<b<c or a>b>c) :
#     print(2*a, 2*b, 2*c)
# else :
#     print(-1*a, -1*b, -1*c)

# 18
# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))
# if (a!=b and a!=c and b==c):
#     print(1)
# elif (b!=a and b!=c and a==c):
#     print(2)
# elif (c!=a and c!=b and a==b):
#     print(3)
#19
# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))
# d=int(input("d="))
# if (a!=b and a!=c and a!=d and b==c==d):
#     print(1)
# elif (b!=a and b!=c and b!=d and a==c==d):
#     print(2)
# elif (c!=b and c!=a and c!=d and b==a==d):
#     print(3)
# elif (d!=b and d!=c and d!=a and b==c==a):
#     print(4)

#20
# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))
# if abs(a-b)<abs(a-c):
#     print(" a ga b eng yaqini")
# elif abs(a-b)>abs(a-c):
#     print(" a ga c eng yaqini")
# else:
#     print("masofalar teng")

# 21
# x=int(input("x="))
# y=int(input("y="))
# ox=0
# oy=0
# if x==0 and y==0:
#     print(0)
# elif x==0 and y!=0:
#     print(2)
# elif y==0 and x!=0:
#     print(1)
# else:
#     print(3)

# 22
# x=int(input("x="))
# y=int(input("y="))
# if x>0 and y>0:
#     print("1-chorak")
# elif x<0 and y>0:
#     print("2-chorak")
# elif x<0 and y<0:
#     print("3-chorak")
# elif x>0 and y<0:    
#     print("4-chorak")

# 23
# a=int(input("x="))
# b=int(input("y="))
# c=int(input("y="))
# d=int(input("y="))

from math import*
# 24
# x=float(input("x="))
# if x>0:
#     print(2*sin(x))
# if x<=0:
#     print(x-6)

# # 25
# x=float(input("x="))
# if x<-2 or x>2:
#     print(2*x)
# else:
#     print(-3*x)

# 26
# x=float(input("x="))
# if x<=0:
#     print(-x)
# if 0<x<2:
#     print(x**2)
# if x>=2:
#     print(4)

# 27
# x=float(input("x="))
# if x<0:
#     print(0)
# if ([x%2==1] and (x%2==0)):
#     print(1)
# if ([x%2==0] and (x%2==1)):
#     print(-1)
# else:
#     print("butun son kirii=ting!")

# 28
yil=int(input("yil="))
if yil%4==0 or yil%400==0:
    print("366 kun")
else:
    print("365 kun")