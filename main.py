def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    if month > 12 or month < 1:  # Если ввели некорктный номер месяца
        return "Invalid month"  # значение функии выводится с данным сообщением.
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:  # если предыдущая функция is_leap True и пользователем выбран 2й месяц
        return 29  # то данные при вызове функции заменяются на кол-во дней в феврале
    return month_days[
        month - 1]  # если предыдущая функция is_leap False, выводится кол-во дней из списка month_days с индеком введенного пользователем месяца минус 1, т.к. в списке отсчет начинается с 0.


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)








