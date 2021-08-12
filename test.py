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
one_day = timedelta(days = 1)
yesterday = current_date - one_day
print('yesterday : ' + str(yesterday))
