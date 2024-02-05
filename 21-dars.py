# numbers=1,2,3
# names='Anna','Zohida','Komila','Zohida'
# print(numbers,type(numbers))
# print(names,type(names))

# names[1]='ozoda'
# print(names)
# del names
# print(names)

# print(names[:2])
# print(names[1:])
# print(names[1:3])
# print(names[:])
# print(names[::-1])
# print(names[::2])

# names2=('Aziza','Halima')
# print(names+names2)
# print(names.count('Zohida'))
# print('Zohida' in names)
# print('Zohid' not in names)

# print(names.index('Komila'))

# namelist=list(names)
# namelist.append('Akobir')
# namelist.insert(0,'Jahongir')
# namelist.remove('Anna')
# names=tuple(namelist)
# print(names)

# talaba={
#     'ism':'Murodil',
#     'familya':'Rahmataliyev',
#     'yosh':20,
#     'Grand':True,
#     'Yo\'nalishi':'ATT'
# }

# print(talaba,type(talaba))
# print(talaba.keys())
# print(talaba.values())
# print(talaba.items())

# for key,value in talaba.items():
#     print(key,value)

# print(talaba.get('ism','bu key mavjud emas'))

# talaba['yosh']=21
# talaba.update({'yosh':22})

# talaba.pop('yosh')
# talaba.popitem()
# del talaba['ism']
# print(talaba)

# numbersset={1,2,3,4,5,2,1,3}
# numbersset={True,2,3,4,5,1,0,False}
# print(numbersset)

# names={'Aziza','Halima','Otabek','Jamolxon'}
# names.pop()
# names.add('Zuhra')
# names.clear()
# print(names)

lang={'python','js','php','c++','react','laravel'}
lib={'django','react','laravel','qtcreator','php','c++'}

# union=lang.union(lib)
# union2=lang | lib
# print(union)
# print(union2)

# interection=lang.intersection(lib)
# interection2=lang & lib
# print(interection)
# print(interection2)

symmetric=lang.symmetric_difference(lib)
symmetric2=lang ^ lib
print(symmetric)
print(symmetric2)










