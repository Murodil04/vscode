# fname="Alisher"
# sname="Karimov"
# age=25
# print(fname,sname)
# print(fname,sname,str(age))

# txt="O\"zbekiston \t\"vatanim\"mani "
# txt2="O\"zbekiston vatanim\bmani "
# txt3="O\"zbekiston \fvatanimmani "
# print(txt,txt2,txt3)

# txt="Hello World"
# print(txt[2])
# print(txt[-1])
# print(txt[1:5])
# print(txt[1:])
# print(txt[:5])
# print(txt[:])

# txt="Hello World"
# print("l" in txt)
# print("z" not in txt)

# value=input("qiymat kiriting:")
# if value.isdigit():
#     natija=int(value)**2
# else:
#     natija='son kiriting'
# print(natija)

# txt='Python dasturlash tili'
# natija=txt.split(' ')
# print(natija)
# print(natija[-1])

# txt='Python dasturlash tili'
# for letters in txt:
#     print(letters)
    
# for index in range(len(txt)):
#     print(index,txt[index])

# txt='Python dasturlash tili'
# arr=txt.split(' ')
# max_el=arr[0]
# for i in arr:
#     if len(max_el)<len(i):
#         max_el=i
# print(max_el)

n=int(input("n="))
kopaytma=0
while kopaytma<=n:
    if kopaytma*kopaytma<=n:
        natija=kopaytma
    kopaytma+=1
print(natija)



