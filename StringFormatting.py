'''
format()Метод позволяет форматировать отдельные части строки.

Иногда есть части текста, которые вы не контролируете, возможно, они взяты из базы данных или введены пользователем?

Чтобы управлять такими значениями, добавьте {}в текст заполнители (фигурные скобки ) и пропустите значения с помощью format()метода:
'''


price = 49
txt = "The price is {} dollars"
print(txt.format(price))

#txt = "The price is {:.2f} dollars"

#print(txt.format(price, itemno, count))

'''
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))
'''

'''
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))
'''

