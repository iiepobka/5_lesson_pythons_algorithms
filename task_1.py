# Пользователь вводит данные о количестве предприятий, их наименования и прибыль
# за 4 квартал (т.е. 4 числа) для каждого предприятия. Программа должна определить
# среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
# предприятий, чья прибыль выше среднего и ниже среднего.
import collections

count_of_factory = int(input('Введите целим числом кол-во предприятий: '))
factories = collections.defaultdict(list)
QWARTER = 4

for i in range(count_of_factory):
    name_of_factory = input(f'Введите наименование {i + 1}-го предприятия: ')
    for j in range(QWARTER):
        profit_of_factory = float(input(f'Введите цифрой прибыль {i + 1}-го предприятия за {j + 1}-й квартал: '))
        factories[name_of_factory].append(profit_of_factory)
    factories[name_of_factory].append(sum(factories[name_of_factory]))

middle_profit = 0
for v in factories.values():
    middle_profit += v[4]
middle_profit = round(middle_profit / count_of_factory, 2)
print(f'Седняя прибыль за год (для всех предприятий): {middle_profit}')

print('Предприятия с годовой прибылью выше или равного среднегодовому значению:')
for k, v in factories.items():
    # >= т.к. ничего не будет выведено при вводе данных одной компании или одинаковых данных у разных компаний
    if v[4] >= middle_profit:
        print(k)

print('Предприятия с годовой прибылью ниже среднего значения:')
for k, v in factories.items():
    if v[4] < middle_profit:
        print(k)


