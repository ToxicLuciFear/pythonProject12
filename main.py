import time
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
name = "Артём"
print(name)
age = 18
print("Мне", age, "лет")
name5 = "Артём " * 5
print(name5)
un = input("Введите ваше имя ")
ua = int(input("Введите ваш возраст "))
print("Ну здарова ", un)
if ua > 50:
    print("Ты что дед?")
elif ua < 6:
    print("А где твои родители")
elif 6 < ua < 18:
    print("А что по матеше задали?")
elif 17 < ua < 50:
    print("Сколько зарабатываешь")
e6 = len(un)
print(un[1:e6 - 1:])
print(un[::-1])
print(un[-3::])
print(un[:5:])
print("Длина имени", len(un))
print("Сумма цифр возраста=", (ua // 10) + (ua % 10), "А их произведение=", (ua // 10) * (ua % 10))
nu = str(str.upper(un))
nl = str(str.lower(un))
nul = nu[0:1:] + nl[1::]
nlu = nl[0:1:] + nu[1::]
print(nu, nl, nul, nlu)
a = 0
spaces = 0
for i in range(0, len(un)):
    if un[i] == ' ':
        print("Пробел в имени не допустим")
        spaces += 1
        break
    else:
        spaces = 0
if spaces == 0:
    print("Имя введено правильно")
if ua > 150 or ua < 0:
    print("Вы ввели не корректный возраст")
else:
    print("Возраст введён правильно")
print("\033[H\033[J")
print("Помоги решить плиз")
print("1/2*x*y+(47-x-y)*(x/3+y/4)")
v = int(input())
if v == 282:
    print("Ты что киборг???????????????")
else:
    print("Ну.........ты хотя бы попытался)")
time.sleep(2)
