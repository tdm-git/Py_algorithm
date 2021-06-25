"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа)
для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести
наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже
среднего.
"""
import collections

company = collections.namedtuple('company', ['name', 'sale', 'sum_sale'])  # используем имменнованый кортеж
# sum_sale - добавим значение общей суммы, т.к. оно будет использоваться несколько раз по ходу задачи
company_count = int(input('введите кол-во предприятий - '))
if company_count:  # если ввели нулевое значение
    company_list = []
    for c in range(company_count):
        com_name = input('введите название компании - ')
        com_sale = list(map(float, input('введите значения прибыли (4 числа разделенных пробелами) - ').split()))
        company_list.append(company(name=com_name, sale=com_sale, sum_sale=sum(com_sale)))
    # print(company_list)
    all_sale = sum([i.sum_sale for i in company_list])  # посчитаем общую сумму
    avg_sale = round(all_sale/company_count, 2)  # и среднее значение
    print(f'средняя прибыль для указанного списка предприятий составила - {avg_sale}')
    good_company = []  # по условиям задачи нужно вывести отдельные списки
    bad_company = []
    for c in company_list:
        if c.sum_sale >= avg_sale:
            good_company.append(c.name)
        else:
            bad_company.append(c.name)
    if len(good_company):  # может и не было
        print(f'список компаний с прибылью выше или равна среднему значению - ', ",".join(good_company))
    if len(bad_company):
        print(f'список компаний с прибылью ниже среднего значения - ', ",".join(bad_company))


