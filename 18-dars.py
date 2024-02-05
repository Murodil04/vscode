# satr26
# txt="Hello world"
# n=3
# diff=abs(len(txt)-n)
# if len(txt)>n:
#     res=txt[diff:]
# else:
#     res=f'{diff*"."}{txt}'
# print(res)

# str27
# txt="Hello world"
# txt2="salom dunyo"
# n=9
# n2=5
# m=txt[:n]
# c=abs(len(txt2)-n2)
# d=txt2[c:]
# print(m+d)
 
# str28
# 1-usul
# txt="Hello world"
# c='o'
# res=txt.replace(c,2*c)
# print(res)

# 2-usul
# txt="Hello world"
# c='o'
# res=""
# for i in txt:
#     if c==i:
#         res+=2*c
#     else:
#         res+=i
# print(res)

# str41
# txt="I love python"
# arr=txt.split(" ")
# print(len(arr),arr)

# str42
txt="I lovel python kiyik".upper()
arr=txt.split(" ")
count=0
for word in arr:
    if word[0]==word[-1]:
        print(word)
        count+=1
print(f'{count}')

# str43
# txt="I loval python apple azard".upper()
# arr=txt.split(" ")
# count=0
# for word in arr:
#     if 'A' in word:
#         print(word)
#         count+=1
# print(f'{count}')

# # str44
# txt="I laovala python appalea azard".upper()
# arr=txt.split(" ")
# count=0
# for word in arr:
#     if word.count("A")==3:
#         print(word)
#         count+=1
# print(f'{count}')

# # str45,46
# txt="laovala python appalea azard".upper()
# arr=txt.split(" ")
# smallword=arr[0]
# for i in arr:
#     if len(smallword)>len(i):
#         smallword=i
# print(smallword)# 

# str47
# txt="laovala python appalea azard".upper()
# print(txt.replace(' ','.'))

# str48
# txt="I loval python apple azard".upper()
# words=txt.split(" ")
# result=[]
# for word in words:
#     f_element=word[0]
#     res=f_element
#     for index in range(1,len(word)):
#         if f_element==word[index]:
#             res+='.'
#         else:
#             res+=word[index]
#     result.append(res)
# print(' '.join(result))

# txt="lavala   ok python  apple azarda"
# words=txt.split(" ")
# print(words)
# result=[]
# for word in words:
#     if word!='':
#         result.append(word)
# print(' '.join(reversed(result)))
# print(' '.join(result[::-1]))
# print(' '.join(sorted(result)))

# txt="lavala ok python apple azarda"
# words=txt.split(" ")
# result=[]
# for word in words:
#     if word[0].islower():
#         word[0]=word[0].upper
#         result.append(word)
# print(' '.join(result))

# ord chr
# print(chr(92))
# print(ord('@'))

# txt="LaVala ok Python apple azarDa"
# count=0
# for i in txt:
#     if i.isupper():
#     if ord(i)