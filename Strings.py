'''
Строки - это массивы
Как и во многих других популярных языках программирования, строки в Python представляют собой массивы байтов, представляющих символы Юникода.

Однако в Python нет символьного типа данных, отдельный символ - это просто строка длиной 1.

Квадратные скобки могут использоваться для доступа к элементам строки.
'''

print("Hello")
print('Hello')

#a = "Hello"
#print(a)

#a = """Lorem ipsum dolor sit amet,
#consectetur adipiscing elit,
#sed do eiusmod tempor incididunt
#ut labore et dolore magna aliqua."""
#print(a)

#a = '''Lorem ipsum dolor sit amet,
#consectetur adipiscing elit,
#sed do eiusmod tempor incididunt
#ut labore et dolore magna aliqua.'''
#print(a)

#Цикл по строке
#Поскольку строки являются массивами, мы можем перебирать символы в строке с помощью forцикла.

'''
for x in "banana":
  print(x)
'''

#Длина строки
#Чтобы получить длину строки, используйте len()функцию.
#len()Функция возвращает длину строки:

'''
a = "Hello, World!"
print(len(a))
'''

#Проверить строку
#Чтобы проверить, присутствует ли в строке определенная фраза или символ, мы можем использовать ключевое слово in.

#пример
#Проверьте, присутствует ли слово «бесплатно» в следующем тексте:

'''
txt = "The best things in life are free!"
print("free" in txt)
'''

#Используйте это в ifзаявлении:
#Печатать только при наличии слова «бесплатно»:

'''
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
'''

#Проверьте, НЕ
#Чтобы проверить, НЕ присутствует ли определенная фраза или символ в строке, мы можем использовать ключевое слово not in.
#Проверьте, НЕ присутствует ли "дорого" в следующем тексте:

'''
txt = "The best things in life are free!"
print("expensive" not in txt)
'''

#Используйте это в ifзаявлении:
#печатать, только если "дорого" НЕТ:

'''
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("Yes, 'expensive' is NOT present.")
'''