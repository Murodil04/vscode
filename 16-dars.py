# while - 6
# n = int(input("n ni kiriting: "))
# fac = 1
# while n > 0:
#   fac *=n
#   n -=2
# print(fac)

# while - 9
# n = int(input("n ni kiriting: "))
# i = 0
# while i<n:
#   if 3**i > n:
#     natija = i
#     break
#   i +=1
# print(natija)

# while - 10
# n = int(input("n ni kiriting: "))
# i = 0
# while i<n:
#   if 3**i <= n: # 0, 1, 2, 3
#     natija = i
#   i +=1
# print(natija)

# while - 13
# a = int(input("a sonni kiriting: ")) # 2
# k = 1
# summa = 0 
# while True:
#   if summa >= a: 
#     print(f"summa = {summa}, k = {k-1}") 
#     break
#   summa +=1/k
#   k +=1 # 4 5

# while - 15
# s = int(input("s ni kiriting: "))
# p = int(input("p ni kiriting: "))
# oy = 0
# a = 2*s
# while s < a:
#   s +=s*p/100
#   oy += 1
# print(f"s={s} , oy ={oy}")

# while - 18
# n = int(input("n ni kiriting: ")) #167
# while n>0:
#   i = n%10 #7, 6 , 1
#   n = n//10 # 16 , 1 ,0
#   print(i,end='')
  
# while - 20
# n = int(input("n ni kiriting: ")) #312
# while n>0:
#   i = n%10 #2 1 3
#   n = n//10 # 31 3 ,0 
#   if i == 2:
#     natija = "2 bor"
#     break
#   else:
#     natija = "2 yo'q"
# print(natija)
    
# while - 23
# EKUB
# a = int(input("a ni kiriting: ")) # 10 , 3
# b = int(input("b ni kiriting: ")) # 7 
# while a != b:
#   if a > b:
#     a -=b
#   else:
#     b -=a
# print(a)

# EKUK
# a = int(input("a ni kiriting: ")) # 10 , 3
# b = int(input("b ni kiriting: ")) # 7 
# c = a*b
# while a != b:
#   if a > b:
#     a -=b
#   else:
#     b -=a
# print(c/a)

# while - 24
# n = int(input("n ni kiriting: "))
# fib = [1,1]
# i = 2
# while i < n:
#   fib.append(fib[i-1]+fib[i-2])
#   if n == fib[i]:
#     natija = f'{n} soni fibonachchi sonlari ichida bor'
#     break
#   else:
#     natija = f"{n} soni fibonachchi sonlari ichida yo'q"
#   i +=1
# print(natija)

# while - 25
n = int(input("n ni kiriting: "))
fib = [1,1]
i = 2
while i <= n:
  fib.append(fib[i-1]+fib[i-2])
  if n < fib[i]:
    natija = fib[i]
    break
  i +=1
print(natija, fib)

