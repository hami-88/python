firstN = 'hamed '
lastN = 'namvar '
output = f'hello, {firstN}{ lastN}'
print(output)
days = 30
print(str(days)+' oridibehesht')
# Fno = input('First No : ')
# Lno = input('Last No : ')
# print(int(Fno) ** int(Lno))
from datetime import datetime, timedelta
current_date = datetime.now()
print('today is: ' + str(current_date))
print('day: ' + str(current_date.day))
print('month: ' + str(current_date.month))
print('year: ' + str(current_date.year))
print('hour: ' + str(current_date.hour))
print('minute: ' + str(current_date.minute))
print('second: ' + str(current_date.second))
one_day = timedelta(days = 1)
yesterday = current_date - one_day
print('yesterday : ' + str(yesterday))
#birthday = input('your birthday (dd/mm/yyyy)')
#birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
#print('birthday: ' + str(birthday_date))

price = input('how much did you pay?')
price = float(price)
if price >= 1.00:
    tax = .07
    print('tax rate is: ' + str(tax))
else:
        tax = 0
        print('tax rate is: ' + str(tax))