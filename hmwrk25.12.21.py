"""Написать программу, решающую задачу:
Ежемесячная стипендия студента составляет, educational_grant руб.,
а расходы на проживание превышают стипендию и, составляют expenses руб. в месяц.
Рост цен ежемесячно увеличивает расходы на, 3%, кроме первого месяца
Составьте программу расчета суммы денег, которую, необходимо единовременно попросить у родителей,
чтобы можно было прожить, учебный год (10 месяцев), используя только эти деньги и стипендию.
Формат вывода:
Студенту надо попросить ХХХ.ХХ рублей"""


def remove_floating(numb):
    # топорно убираем плавающую точку TODO
    numb = int(numb * 100) / 100
    return numb


educational_grant = int(input('(в рублях)\nЕжемесячная стипендия студента составляет:'))
expenses = int(input('(в рублях)\nрасходы на проживание составляют:'))
study_year = int(10)
counter = 0
required_percentage = expenses / 100 * 3
required_percentage = remove_floating(required_percentage)


if educational_grant > expenses:
    print('увы, но стипендия должна быть меньше, чем ваши затраты:((')
    exit()

while counter != study_year:
    expenses = expenses + required_percentage
    counter += 1


# убираем один месяц
expenses = expenses - required_percentage
expenses = remove_floating(expenses)
# print(expenses)

answer = int(expenses - educational_grant)

print('Студенту надо попросить', answer, 'рублей')
