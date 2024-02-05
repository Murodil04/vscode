# binary=[
#     [0,0,0,1,0,0,0],
#     [0,0,1,1,1,0,0],
#     [0,1,1,1,1,1,0],
#     [1,1,1,1,1,1,1],
#     [0,0,1,1,1,0,0],
#     [0,0,1,1,1,0,0],
#     [0,0,1,1,1,0,0],
# ]
# takror=0
# for list in binary:
#     for i in list:
#         if i==1:
#             i='*'
#         if i==0:
#             i=' '
#         print(i,'',end='')
#     print('')

# array_1
# n=int(input("n="))
# toq=[]
# for i in range(1,n):
#     if i%2==1:
#         toq.append(i)
# print(toq)

# array_2
# n=int(input("n="))
# k=[]
# for i in range(0,n):
#         x=2**i
#         k.append(x)
# print(k)

# array_3
# a=int(input("a="))
# d=int(input("d="))
# n=int(input("n="))
# l=[]
# for i in range(n):
#     x=a+i*d
#     l.append(x)
# print(l)


# array_4
# a=int(input("a="))
# d=int(input("d="))
# n=int(input("n="))
# l=[]
# for i in range(1,n+1):
#     x=a*d*i
#     l.append(x)
# print(l)

# array_5
# # 1-usul
# list=[1,1]
# n=int(input("n="))
# for i in range(2,n):
#     element=list[i-1]+list[i-2]
#     list.append(element)
# print(list)
# 2-usul
# n=10
# a,b=0,1
# for i in range(n):
#     a,b=b,a+b
#     print(a,end=',')

# array_6
# list=['A','B']
# n=int(input("n="))
# sum=0
# for i in range(2,n):
#     sum+=i
#     list.append(sum)
# print(list)
# n=10
# a=2
# b=4
# fib_list=[a,b]
# for i in range(2,n):
#     s=0
#     for j in range(i):
#         s+=fib_list[j]
#     fib_list.append(s)
# print(fib_list)

# array_7
# list=[]
# n=int(input("n="))
# for i in range(n):
#     # print(i)
#     list.append(i)
# list.reverse()
# print(list)
# print("========================")
# n=10
# numbers=list(range(10))
# print(numbers[::-1])

# array_8
# list=[]
# n=[4,5,7,8,6,9]
# for i in n:
#     if i%2==1:
#         list.append(i)
# print(f"{list} toq sonlar {list.__len__()} ta")
# count=0
# numbers=[4,5,7,8,6,9]
# for i in numbers:
#     if i%2==1:
#         print(i,end=' ')
#         count+=1
# print(f"count={count}")
# print("========================")
# array_9
# list=[]
# n=[4,5,7,8,6,9]
# for i in n:
#     if i%2==0:
#         list.append(i)
# list.reverse()
# print(f"{list} juft sonlar {list.__len__()}")
# count=0
# numbers=[4,5,7,8,6,9]
# for i in range(len(numbers)-1,-1,-1):
#     if numbers[i]%2==0:
#         print(numbers[i],end=' ')
#         count+=1
# print(f"count={count}")
# print("========================")

# array_10
# list=[]
# n=[4,5,7,8,6,9]
# for i in n:
#     if i%2==1:
#         list.append(i)
# list.reverse()
# for i in n:
#     if i%2==0:
#         list.append(i) 
# print(list)

# array_11
# numbers=[4,5,7,8,6,9]
# k=2
# for i in range(k,len(numbers),k):
#     print(numbers[i])

# array_13
# numbers=[4,5,7,8,6,9]
# for i in range(len(numbers)-2,-1,-2):
#     print(numbers[i])

# array_14
# numbers=[4,5,7,8,6,9]
# print(numbers[::2])
# print(numbers[1::2])

# array_15
# numbers=[4,5,7,8,6,9]
# print(numbers[1::2])
# print(numbers[-2::-2])

# # array_18
# array=[3,34,56,76,55,2,23,43,28]
# for i in range(len(array)):
#     if array[-1]>array[i]:
#         natija=array[i]
#         break
# else:
#     natija=0
# print(natija)

# array_19
# array=[3,34,56,7,55,2,23,43,36]
# for i in range(len(array)-1,0,-1):
#     if array[0]<array[i] and array[i]<array[-1]:
#         natija=i
#         break
# else:
#     natija=0
# print(natija)

# array_20
# n=[1,2,3,4,5,6,7]
# k=int(input("k="))
# l=int(input("l="))
# sum=0
# for i in range(k,l+1):
#     sum+=n[i]
# print(sum)

# # array_21
# n=[1,2,3,4,5,6,7]
# k=int(input("k="))
# l=int(input("l="))
# sum=0
# a=0
# for i in range(k,l+1):
#     sum+=n[i]
#     a+=1
# print(sum/a)

# array_22/23
# n=[1,2,3,4,5,6,7,8,9,10]
# k=int(input("k="))
# l=int(input("l="))
# print(n[:k]+n[l+1:])
# sum=0
# count=0
# for i in (n[:k]+n[l+1:]):
#     sum+=i
#     count+=1
# print(sum)
# print(sum/count)

# array_24
# array=[1,3,5,7,9,11]
# ayirma=array[1]-array[0]
# arifmetik=0
# for i in range(2,len(array)):
#     if ayirma!=array[i]-array[i-1]:
#         arifmetik=1
# if arifmetik==0:
#     print(ayirma)
# else:
#     print(0)


# array_25
# array=[3,6,12,24,48]
# kopaytma=array[1]/array[0]
# geometik=0
# for i in range(2,len(array)):
#     if kopaytma!=array[i]/array[i-1]:
#         geometik=1
# if geometik==0:
#     print(kopaytma)
# else:
#     print(0)

# # array_26
# array=[2,5,6,9,4,3,90,11]
# for i in range(len(array)-1):
#     if array[i]%2==array[i+1]%2:
#         natija=i+1
#         break
#     else:
#         natija=0
# print(natija)


# array_27
array=[-2,5,-6,9,-4,3,-90,11]
for i in range(len(array)-1):
    if array[i]>0 and array[i+1]>0 or (array[i]<0 and array[i+1]<0):
        natija=i+1
        break
    else:
        natija=0
print(natija)



