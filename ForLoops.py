'''
Цикл for используется для перебора последовательности (то есть списка, кортежа, словаря, набора или строки).

Это меньше похоже на ключевое слово for в других языках программирования и больше похоже на метод итератора, 
как в других объектно-ориентированных языках программирования.

С помощью цикла for мы можем выполнить набор операторов один раз для каждого элемента в списке, кортеже, наборе и т. Д.
'''
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#Даже строки являются повторяемыми объектами, они содержат последовательность символов:

'''
for x in "banana":
  print(x)
'''

#С помощью оператора break мы можем остановить цикл до того, как он пройдёт через все элементы:

'''
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
'''
#Выйдите из цикла, когда xбудет "банан", но на этот раз разрыв будет перед печатью:

'''
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
''''

#С помощью оператора continue мы можем остановить текущую итерацию цикла и продолжить следующую:

'''
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
'''

#Чтобы перебрать набор кода указанное количество раз, мы можем использовать функцию range () ,
#Функция range () возвращает последовательность чисел, начиная с 0 по умолчанию и увеличивая на 1 
#(по умолчанию) и заканчивая указанным числом.

'''
for x in range(6):
  print(x)
'''

#Функция range () по умолчанию имеет значение 0 в качестве начального значения, 
#однако можно указать начальное значение, добавив параметр: range (2, 6) , 
#что означает значения от 2 до 6 (но не включая 6):

'''
for x in range(2, 6):
  print(x)
'''

#По умолчанию функция range () увеличивает последовательность на 1,
#однако можно указать значение приращения, добавив третий параметр: range (2, 30, 3 ) :

'''
for x in range(2, 30, 3):
  print(x)
'''

#elseКлючевое слово в forцикле определяет блок кода , который будет выполняться , когда цикл завершен:

'''
for x in range(6):
  print(x)
else:
  print("Finally finished!")
'''

#Разорвите цикл, когда xбудет 3, и посмотрите, что произойдет с elseблоком:

'''
or x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
'''
#Вложенный цикл - это цикл внутри цикла.

#«Внутренний цикл» будет выполняться один раз для каждой итерации «внешнего цикла»:


'''
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
'''

#forциклы не могут быть пустыми, но если по какой-то причине у вас 
#есть forцикл без содержимого, введите passоператор, чтобы избежать ошибки.

'''

for x in [0, 1, 2]:
  pass
'''