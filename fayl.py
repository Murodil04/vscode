##########_____fayllar bilan ishlash
# x-create
# w-write
# a-append
# r-read
# fayl=open('test.txt','x')
# print('Fayl yaratildi')

# fayl=open('test.txt','a')
# fayl.write('Happy new year...')
# fayl.write('\nAssalomu aleykum \n')
# fayl.close
# print('Faylga yozildi')

# fayl=open('test.txt','r')
# data=fayl.read(10)
# data=fayl.readlines()
# print(data)
# fayl.close

# fayl=open('test.txt','r')
# data=fayl.readlines()
# for i in data:
#     print(i.replace('\n',''))
# fayl.close

path="D:/test.txt"
fayl=open(path,'w')
fayl.write('Salom')
fayl.close
print(path)
# path="D:/lesson/HYBRID.PY/lessons/"
# lessons=int(input('lessonnumber:'))
# themeN=input('Theme name:')
# fayl=open(f'{path}{lessons}-lesson.txt','w')
# fayl.write(f'{lessons}-Theme is {themeN}')
# fayl.close
# print('File created successfully')

# print(".")




