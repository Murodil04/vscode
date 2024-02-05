# # 1_fya
# def powera3(number):
#     return number**3
# print(powera3(3.4))
# print(powera3(4))

# 2_fya
# def powera234(res):
#     return res
# print(powera234(2))
# print(powera234(4))


# # 6_fya
# def digitcountsum(number):
#     count=0
#     yigindi=0
#     while (number>0):
#         count+=1
#         yigindi+=number%10
#         number=number//10
#         result=f'count-{count} ,sum-{yigindi}'
#     return result
# print(digitcountsum(int(input('number kiriting:'))))


# # 7_fya
# def digitcountsum(number):
#     count=0
#     teskari=0
#     while (number>0):
#         count+=1
#         teskari=teskari*10+number%10
#         number=number//10
#         result=f'count-{count} ,sum-{teskari}'
#     return result
# print(digitcountsum(int(input('number kiriting:'))))

# 9_fya
# def digitcountsum(number,k):
#     temp=number
#     count=1
#     while (number>0):
#         count*=10
#         number=number//10
#     result=k*count+temp
#     return result

# print(digitcountsum(int(input('number kiriting')),int(input('k ni kiriting'))))

# # 12_fya
# def son(a,b,c):
#     if a<=b and b<=c:
#         a,b,c=a,b,c
#     elif a<=c and c<=b:
#         a,b,c=a,c,b
#     elif b<=c and c<=a:
#         a,b,c=b,c,a
#     elif b<=a and a<=c:
#         a,b,c=b,a,c
#     elif c<=a and a<=b:
#         a,b,c=c,a,b
#     elif c<=b and b<=a:
#         a,b,c=c,b,a
#     result=a,b,c
#     return result 
# print(son (a=int(input('a kiriting')),b=int(input('b ni kiriting')),c=int(input('c ni kiriting'))))
 
# 24_fya
# def isSquare(k):
#     res=k**(1/2)%1==0
#     return res
# print(isSquare(24))

# # 26_fya
# def isPower(k):
#     while (k>5):
#         k=k//5
#     return k==5
# print(isPower(25))

# 26_fya
def isPower(k):
    i=1
count=0
while (i<=5):
    res=isPower(int(input('k:')))
    # return k=5
print(isPower(25))



