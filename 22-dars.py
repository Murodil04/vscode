# def greeting(name,age):
#     print(f"{name} {age} yosh")
# greeting(age=19,name='Hasan')

# def greeting(name='Anna'):
#     print(f"Hello {name} ")
# greeting('Hasan')
# greeting()

# def square(number):
#     res=f'{number**2},{number**3}'
#     return res
# num=int(input("enter a num="))
# print(square(num))

# result=square(num)
# print(result)

# def getmax(*nums):
#     return max(nums)
# print(getmax(3))
# print(getmax(3,7,-2))
# print(getmax(3,66,94,23))
# print(getmax(3,23,34,4,90))

# def calc(num1,num2,num3):
#     num1+=num2
#     return num1/num3
# print(calc(num1=3,num2=7,num3=5))

# def calc(**nums):
#     result=nums['num1']+nums['num2']+nums['num3']
#     return result
# print(calc(num1=3,num2=7,num3=5))

# def about(**user):
#     result=f"Email:{user['email']},{user['username']},{user['phone']}"
#     return result
# print(about(email='rahmataliyev15@gmail.com',username='mr_0824',phone='a53'))


# def greeting(name,age):
#     '''
#     Bu funksiya berilgan qiymat boyicha
#     bizga javob qaytaradi va 2 ta parametr
#     qabul qiladi bular name va age '''
#     print(f'Hello,{name}-{age}')
# print(greeting.__doc__)
# help(greeting)

# def getAge(now):
#     global year
#     year=2004
#     return now-year
# print(getAge(2023))
# print(year)
