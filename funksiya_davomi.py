# def calc(a,b):
#     return(a+b)
# print(calc(4,5))

# lambda_calc=lambda a,b:a+b
# print(lambda_calc(4,5))

# lanbda_max=lambda a,b:print('a') if a>b else print('b')
# lanbda_max(3,8)

# def getVowels(letter):
#     vowels=['a','o','e','i','u']
#     if letter in vowels:
#         return letter
# # print(getVowels(input('enter a letter')))
# values=['a','b','c','u','i','e','t']
# filtered=filter(getVowels,values)
# print(list(filtered))


# numbers=list(range(1,35))
# filter_square=filter(lambda x:x>7 and x<20,numbers)
# print(list(filter_square))

# numbers=list(range(1,35))
# def square (num):
#     if num%2==0:
#         return num*num
# map_square2=map(square,numbers)
# print(list(map_square2))

# numbers=list(range(1,35))
# map_square=map(lambda x:x*x,numbers)
# print(list(map_square))


# zip function
# programs=['python','javascript','php','html']
# libraries=['django','react','laravel','bootstrap']
# salaries=[1000,1500,1100,1400]
# zip_mix=zip(programs,libraries,salaries)
# print(list(zip_mix))

# numbers=[1,2,3,4,5]
# numbers2=[6,7,8,9,8]

# result=[]
# for i in range(len(numbers)):
#     result.append(numbers[i]+numbers2[i])
# print(result)

# map_cals=list(map(lambda x,y:x+y,numbers,numbers2))
# print(map_cals)

# zip_calc=[sum(value) for value in zip(numbers,numbers2)]
# print(zip_calc)

from functools import reduce
import numbers
def accumulator (summa,num):
    return summa+num
res=reduce(accumulator,numbers,0)
print(res)

reduce_cals=reduce(lambda summa,num:summa+num,numbers,0)
print(reduce_cals)


