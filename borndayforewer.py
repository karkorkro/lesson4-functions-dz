"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""
# Было:
"""
year = input('Ввведите год рождения А.С.Пушкина:')
while year != '1799':
    print("Не верно")
    year = input('Ввведите год рождения А.С.Пушкина:')

day = input('Ввведите день рождения Пушкин?')
while day != '6':
    print("Не верно")
    day = input('В какой день июня родился Пушкин?')
print('Верно')
"""

# Мое решение

def check_answer(answer_entered, correct_answer):
    if answer_entered == correct_answer:
        print('Верно')
    else:
        print('Неверно')
    return answer_entered == correct_answer


def ask_smth(question):
    answer = input(f'{question}')
    return answer


pshkn = {'В каком году родился Пушкин': '1799', 'В какой день родился Пушкин': '6.06'}

def victory(questions_dict):
    for key in questions_dict.keys():
        answer = ask_smth(key)
        while not check_answer(answer, questions_dict[key]):
            answer = ask_smth(key)

victory(pshkn)