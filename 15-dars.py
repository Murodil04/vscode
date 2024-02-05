# array 18
# array = [12,26,35,3,68,39,29,18,2,15,13,11]
# for i in range(len(array)):
#   if array[-1]>array[i]:
#     natija = array[i]
#     break
# else:
#   natija = 0
# print(natija)

# array 19
# array = [1,32,26,35,3,68,39,29,18,2,15,13,11]
# for i in range(len(array)-1,0,-1):
#   if array[0] < array[i] and array[i] < array[-1]:
#     natija = i
#     break
#   else:
#     natija = 0
# print(natija)

# array - 20
# array = [1,2,3,4,5,6,7,8,9,10]
# k = int(input('k ni kiriting: ')) # 2
# l = int(input('l ni kiriting: ')) # 7
# sum = 0
# for  i in range(k,l+1):
#   sum +=array[i]
# print(sum)  
  
#array - 22,23
# array = [1,2,3,4,5,6,7,8,9,10]
# k = int(input('k ni kiriting: ')) # 2
# l = int(input('l ni kiriting: ')) # 7
# print(array[:k] + array[l+1:])
# sum = 0
# count = 0
# for i in (array[:k] + array[l+1:]):
#   sum += i
#   count +=1
# print(sum/count)

# array - 24,25
# array = [1,3,9,27,81,243]
# kopaytma = array[1]/array[0]
# geometrik = 0 #1
# for i in range(2,len(array)):
#   if kopaytma != array[i]/array[i-1]:
#     geometrik = 1
# if geometrik == 0: #1==0
#   print(kopaytma)
# else:
#   print(0)

# array - 26,27
# array = [2,-1,14,-17,28,-17,36,49]
# for  i in range(len(array)-1):
#   # array[i]%2 == array[i+1]%2
#   if array[i]>0 and array[i+1]>0 or (array[i]<0 and array[i+1]<0):
#     natija = i+1
#     break
#   else:
#     natija = 0
# print(natija)

# while - 2
# a = int(input('a ni kiriting: '))
# b = int(input('b ni kiriting: '))
# count = 0
# while b<=a:
#   a-=b
#   count +=1
# print(count)

# while - 4
# n = int(input('n ni kiriting: '))
# i = 0
# while i<=n:
#   if 3**i == n:
#     natija = f'3 ning {i} darajasi'
#     break
#   else:
#     natija = '3 ning darajasi emas'
#   i+=1
# print(natija)

# while - 6
# n = int(input('n ni kiriting: '))
# kopaytma = 1
# while 0<n:
#   kopaytma *=n
#   n -=2
# print(kopaytma)

# while - 7
# n = int(input('n ni kiriting: ')) #16
# i = 0
# while i<=n: # 0,1,2,3,4,5
#   if i*i > n: # 0*0, 1*1,2*2,3*3,4*4,5*5
#     print(i)
#     break
#   i +=1
  
# while - 8
n = int(input('n ni kiriting: ')) #16
i = 0
while i<=n: # 0,1,2,3,4,5
  if i*i <= n: # 0*0, 1*1,2*2,3*3,4*4,5*5
    # print(i)
    natija = i
  i +=1
print(natija)
