'''
i = 1
while i < 6:
  print(i)
  i += 1
'''

#С помощью оператора break мы можем остановить цикл, даже если условие while истинно:

'''
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
'''

#С помощью оператора continue мы можем остановить текущую итерацию и продолжить следующую:

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#С помощью оператора else мы можем запустить блок кода один раз, когда условие больше не выполняется:

'''
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
'''