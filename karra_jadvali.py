# topshiroq>1-2
# ismlar=['ali','vali','hasan','husan','olim']
# sum=0
# for ism in ismlar:
#     sum+=1
#     print(f"Salom {ism.title()}")
# print(f"Kod {sum} marta takrorlandi")

# topshiroq>3
# for i in range(11,100,2):
#     print(i**3)

# topshiroq>4
# kinolar=[]
# print("5 ta kinoni kiriting:")
# for i in range(1,6):
#     kinolar.append(input(f"{i} -kino nomini kiriting:"))
# print(kinolar)

# topshiroq>5
# for i in range(0,100,7):
#     print(f"{i} ning kivadrati {i**2} ga teng")

# topshiroq>6
# for i  in range(2,10):
#     for j in range(1,9):
#         print(f" {j}x{i}={j*i} | ", end='')
#     print(" ")   

# for i in range(2,10):
#     for j in range(1,10):
#         if i*j<10:
#             print(f'{i}x{j}={i*j}  |  ', end='')
#         else:
#             print(f'{i}x{j}={i*j} |  ', end='')
#     print(' ') 


# topshiroq>7
#  yagonalarini topish
# numbers=[651,25,-78,12,56,25,56]
# element=[]
# for number in numbers:
#     if number not  in element:
#         element.append(number)
# print(element)

# numbers=[1,2,3,4,67,89,1,2,4]
# duplicate_element=[]
# for i in range(len(numbers)):
#     k=i+1
#     for j in range(k,len(numbers)):
#         if numbers[i]==numbers[j]:
#             duplicate_element.append(numbers[i])
# print(duplicate_element)

#kichkinasini topish
# min_element=numbers[0]
# for number in numbers:
#     if number<min_element:
#         min_element=number   
# print(min_element)

# topshiroq>8
# Tub sonlarni chiqarish
# n=int(input("sonni kiriting:"))
# for son in range(1,n+1):
#     count=0
#     for i in range(1,son+1):
#         if son%i==0:
#             count+=1
#     if count==2:
#         print(son)        
    
# n=int(input("sonni kiriting:"))
# count=0
# for son in range(1,n+1):
#     if n%son==0:
#         count+=1
# if count==2:
#     print("Tub son")
# else:
#      print("Tub emas")


