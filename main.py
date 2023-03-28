#модуль3 завдання1
#https://replit.com/@MaryBuriak/HummingSuburbanSandbox#main.py
#Заходжу в Пекарня, купую тут такі товари: ['Хліб', 'Пончик', 'Булки'].
#Їду до Продуктовий, купую такі товари: ['Морква', 'Селера', 'Рукола'].
#Разом купую 6 товарів.

shopping_dict = {
    "пекарня": ["хліб", "пончик", "булки"],
    "продуктовий": ["морква", "селера", "рукола"],
    }

for keys, values in shopping_dict.items():
  print(f"Заходжу в", keys.capitalize(), "купую тут такі товари:", values)

number = (len(shopping_dict["пекарня"])+len(shopping_dict["продуктовий"]))
print("Разом купую", number ,"товарів.")


#модуль3 завдання2
#числа, які діляться на 5
for i in range(1, 101):
  if (i % 5) == 0:
    print(i)
#підносимо до 3ї степені
num3 = [i**3 for i in range(1, 101) if (i % 5) == 0]
print(num3)

print("Hello world!")
print("Hello world!")
print("Hello world!")
