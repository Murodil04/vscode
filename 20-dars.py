# txt=input('satr kiriting:')
# words=txt.split(" ")
# res2=[]
# for word in words:
#     res=word[0].upper()+word[1:].lower()
#     res2.append(res)
# print(''.join(res2))
# 2-usul
# txt=input('satr kiriting:')
# natija=txt.title()
# print(natija)
# 3-usul  chalaaaa
# satr=input('satr kiriting:')
# txt=satr.split()
# arr=[]
# for i in txt:
#     natija=""
#     if ord(i[0]) in range(97,123)
#     son=
# 53
# 1-usul
# satr=input('satr kiriting:')
# belgi=0
# for i in satr:
#     if i.isalnum()==False:
#         belgi+=1
# print(belgi)
# 2-usul
# satr=input('satr kiriting:')
# belgi=0
# for i in satr:
#     if ord(i)>=33 and ord(i)<=47 or ord(i)>=58 and ord(i)>=91 and ord(i)<=96:
#         belgi+=1
# print(belgi)


# funksiyalaar=> ord(),chr()
# print(chr(92))
# print(ord('@'))
# 54
# txt='Loveala Python va applea Azarda ok'
# count=0
# for i in txt:
#     if i.isupper():
#     # if ord(i) in range(65,91):
#         count+=1
# print(txt,count)
# 55
# txt='Loveala Python va appleajgvvj Azarda ok'
# words=txt.split(" ")
# print(words)
# for i in words:
#     res=len(words[0])<len(words[i])
# print(res)

# 58
# satr=f"D:\Qudrat_c++\books\My_book.exe"
# txt=satr.split('\\')
# res=txt[-1].split("\\")

# satr-62
# satr=input("satrni kiriting")
# txt=satr.split()
# arr=[]
# for i in txt:
#     natija=''
#     for j in i:
#         res=ord(j)
#         if res>=65 and res<90 or res>=97 and res<122:
#             natija+=chr(res+1)
#         elif res==90 or res==122:
#             natija=chr(res)
#         else:
#             natija+chr(res)
#     arr.append(natija)
# print(arr)

# satr63
# satr=input("satrni kiriting")
# k=int(input("k="))
# txt=satr.split()
# arr=[]
# for i in txt:
#     natija=''
#     for j in i:
#         res=ord(j)+k
#         if res>=65 and res<90 or res>=97 and res<122:
#             natija+=chr(res)
#         elif res<=90 or res>=122:
#             natija+=chr(res-26)
#         else:
#             natija+=chr(res)
#     arr.append(natija)
# print(" ".join(arr))

# txt='Hello World'
# k=int(input("k="))
# subtext=''
# for belgi in txt:
#     if belgi.isalpha():
#         isupper=belgi.isupper()
#         res=chr((ord(belgi)-ord("A" if isupper else 'a')+k)%26+ord("A" if isupper else 'a'))
#         subtext+=res
#     else:
#         subtext+=belgi
# print(subtext)



